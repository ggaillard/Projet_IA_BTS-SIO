import os
import shutil
import streamlit as st
from pathlib import Path
from typing import List, Optional
try:
    from git import Repo, GitCommandError
    GIT_AVAILABLE = True
except ImportError:
    GIT_AVAILABLE = False
    st.warning("GitPython non installé. Fonctionnalité de clonage désactivée.")

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

# Import des variables de configuration
from app.config import OPENAI_API_KEY, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

class SimpleDocumentIngestor:
    def __init__(self, data_dir: str = "data", vectorstore_dir: str = "vectorstore"):
        self.data_dir = Path(data_dir)
        self.vectorstore_dir = Path(vectorstore_dir)
        self.supported_extensions = {'.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml'}
        
    def clone_repository(self, repo_url: str) -> bool:
        """Clone un repository Git"""
        if not GIT_AVAILABLE:
            st.error("GitPython non installé. Impossible de cloner le repository.")
            return False
            
        try:
            if self.data_dir.exists():
                shutil.rmtree(self.data_dir)
            
            Repo.clone_from(repo_url, str(self.data_dir))
            st.success(f"Repository cloné avec succès depuis {repo_url}")
            return True
            
        except Exception as e:
            st.error(f"Erreur lors du clonage : {e}")
            return False
    
    def load_documents_from_directory(self) -> List[Document]:
        """Charge tous les documents supportés depuis le répertoire data"""
        documents = []
        
        if not self.data_dir.exists():
            st.warning("Le répertoire data n'existe pas")
            return documents
        
        # Compteurs pour les statistiques
        file_counts = {}
        
        for file_path in self.data_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in self.supported_extensions:
                try:
                    loader = TextLoader(str(file_path), encoding="utf-8")
                    docs = loader.load()
                    
                    # Ajouter des métadonnées
                    for doc in docs:
                        doc.metadata.update({
                            'source_file': str(file_path.relative_to(self.data_dir)),
                            'file_type': file_path.suffix.lower(),
                            'file_size': file_path.stat().st_size
                        })
                    
                    documents.extend(docs)
                    
                    # Compter les fichiers par type
                    ext = file_path.suffix.lower()
                    file_counts[ext] = file_counts.get(ext, 0) + 1
                    
                except Exception as e:
                    st.warning(f"Impossible de charger {file_path}: {e}")
        
        # Afficher les statistiques
        if file_counts:
            st.info(f"Fichiers chargés: {dict(file_counts)}")
        
        return documents
    
    def upload_documents(self, uploaded_files) -> List[Document]:
        """Traite les fichiers uploadés via Streamlit"""
        documents = []
        
        # Créer le répertoire uploads s'il n'existe pas
        upload_dir = self.data_dir / "uploads"
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        for uploaded_file in uploaded_files:
            file_path = upload_dir / uploaded_file.name
            
            # Sauvegarder le fichier
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Charger le document (seulement les fichiers texte pour l'instant)
            try:
                if file_path.suffix.lower() in self.supported_extensions:
                    loader = TextLoader(str(file_path), encoding="utf-8")
                    docs = loader.load()
                    
                    # Ajouter des métadonnées
                    for doc in docs:
                        doc.metadata.update({
                            'source_file': uploaded_file.name,
                            'file_type': file_path.suffix.lower(),
                            'uploaded': True
                        })
                    
                    documents.extend(docs)
                else:
                    st.warning(f"Type de fichier non supporté: {uploaded_file.name}")
                
            except Exception as e:
                st.error(f"Erreur lors du traitement de {uploaded_file.name}: {e}")
        
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Découpe les documents en chunks"""
        if not documents:
            return []
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        
        # Ajouter des métadonnées aux chunks
        for i, chunk in enumerate(chunks):
            chunk.metadata['chunk_id'] = i
            chunk.metadata['chunk_size'] = len(chunk.page_content)
        
        return chunks
    
    def create_vectorstore(self, documents: List[Document]) -> Optional[FAISS]:
        """Crée et sauvegarde le vectorstore"""
        if not documents:
            st.error("Aucun document à indexer")
            return None
        
        try:
            # Créer les embeddings
            embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY,
                model=EMBEDDING_MODEL
            )
            
            # Créer le vectorstore
            with st.spinner(f"Création des embeddings pour {len(documents)} chunks..."):
                vectorstore = FAISS.from_documents(documents, embeddings)
            
            # Sauvegarder
            self.vectorstore_dir.mkdir(exist_ok=True)
            vectorstore.save_local(str(self.vectorstore_dir))
            
            st.success(f"Vectorstore créé avec {len(documents)} chunks")
            return vectorstore
            
        except Exception as e:
            st.error(f"Erreur lors de la création du vectorstore: {e}")
            return None
    
    def ingest_from_repo(self, repo_url: str) -> bool:
        """Processus complet d'ingestion depuis un repository"""
        if not self.clone_repository(repo_url):
            return False
        
        documents = self.load_documents_from_directory()
        if not documents:
            st.error("Aucun document trouvé dans le repository")
            return False
        
        chunks = self.split_documents(documents)
        vectorstore = self.create_vectorstore(chunks)
        
        return vectorstore is not None
    
    def ingest_from_uploads(self, uploaded_files) -> bool:
        """Processus complet d'ingestion depuis des fichiers uploadés"""
        documents = self.upload_documents(uploaded_files)
        if not documents:
            return False
        
        chunks = self.split_documents(documents)
        
        # Fusionner avec l'index existant si possible
        try:
            if self.vectorstore_dir.exists():
                embeddings = OpenAIEmbeddings(
                    openai_api_key=OPENAI_API_KEY,
                    model=EMBEDDING_MODEL
                )
                existing_store = FAISS.load_local(str(self.vectorstore_dir), embeddings)
                
                # Créer un nouveau store pour les nouveaux documents
                new_store = FAISS.from_documents(chunks, embeddings)
                
                # Fusionner
                existing_store.merge_from(new_store)
                existing_store.save_local(str(self.vectorstore_dir))
                
                st.success(f"Ajouté {len(chunks)} nouveaux chunks à l'index existant")
            else:
                self.create_vectorstore(chunks)
                
        except Exception as e:
            st.error(f"Erreur lors de la fusion: {e}")
            return False
        
        return True

def ingest_documents(repo_url: str = None, uploaded_files=None) -> bool:
    """Fonction principale d'ingestion"""
    ingestor = SimpleDocumentIngestor()
    
    if repo_url:
        return ingestor.ingest_from_repo(repo_url)
    elif uploaded_files:
        return ingestor.ingest_from_uploads(uploaded_files)
    else:
        # Utiliser les documents existants dans le répertoire data
        documents = ingestor.load_documents_from_directory()
        if documents:
            chunks = ingestor.split_documents(documents)
            return ingestor.create_vectorstore(chunks) is not None
        return False