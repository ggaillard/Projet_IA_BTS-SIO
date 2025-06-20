import os
from typing import Dict, List, Optional, Tuple
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document
import streamlit as st
from app.config import (
    MODEL_NAME, 
    PROVIDER, 
    MISTRAL_API_KEY, 
    MISTRAL_API_BASE,
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    MAX_RESULTS,
    SIMILARITY_THRESHOLD,
    get_model_config
)

class AdvancedQAChain:
    def __init__(self, vectorstore_path: str = "vectorstore"):
        self.vectorstore_path = vectorstore_path
        self.vectorstore = None
        self.qa_chain = None
        self.conversation_history = []
        
    def load_vectorstore(self) -> bool:
        """Charge le vectorstore"""
        try:
            if not os.path.exists(self.vectorstore_path):
                return False
            
            embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY,
                model=EMBEDDING_MODEL
            )
            
            self.vectorstore = FAISS.load_local(self.vectorstore_path, embeddings)
            return True
            
        except Exception as e:
            st.error(f"Erreur lors du chargement du vectorstore: {e}")
            return False
    
    def create_llm(self):
        """Crée le modèle LLM selon la configuration"""
        config = get_model_config()
        
        if PROVIDER == "mistral":
            return ChatOpenAI(
                openai_api_base=config["base_url"],
                openai_api_key=config["api_key"],
                model_name=config["model"],
                temperature=0.7,
                max_tokens=1000
            )
        else:
            return ChatOpenAI(
                openai_api_key=config["api_key"],
                model_name=config["model"],
                temperature=0.7,
                max_tokens=1000
            )
    
    def create_custom_prompt(self, include_history: bool = False) -> PromptTemplate:
        """Crée un prompt personnalisé"""
        if include_history and self.conversation_history:
            history_text = "\n".join([
                f"Q: {item['question']}\nR: {item['answer']}" 
                for item in self.conversation_history[-3:]  # Garder seulement les 3 dernières
            ])
            
            template = """Vous êtes un assistant IA spécialisé dans l'analyse de documents. 
Utilisez les informations suivantes pour répondre à la question de manière précise et détaillée.

Historique de la conversation:
{history}

Contexte actuel:
{context}

Question: {question}

Instructions:
- Répondez uniquement en vous basant sur les informations fournies
- Si vous ne trouvez pas l'information, dites-le clairement
- Citez les sources quand c'est pertinent
- Soyez précis et concis
- Adaptez votre ton à la question posée

Réponse:"""
            
            return PromptTemplate(
                template=template,
                input_variables=["history", "context", "question"]
            )
        else:
            template = """Vous êtes un assistant IA spécialisé dans l'analyse de documents.
Utilisez les informations suivantes pour répondre à la question de manière précise et détaillée.

Contexte:
{context}

Question: {question}

Instructions:
- Répondez uniquement en vous basant sur les informations fournies
- Si vous ne trouvez pas l'information, dites-le clairement
- Citez les sources quand c'est pertinent
- Soyez précis et concis

Réponse:"""
            
            return PromptTemplate(
                template=template,
                input_variables=["context", "question"]
            )
    
    def setup_qa_chain(self, use_history: bool = False):
        """Configure la chaîne QA"""
        if not self.vectorstore:
            raise ValueError("Vectorstore non chargé")
        
        llm = self.create_llm()
        prompt = self.create_custom_prompt(use_history)
        
        # Créer le retriever avec des paramètres personnalisés
        retriever = self.vectorstore.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": MAX_RESULTS,
                "score_threshold": SIMILARITY_THRESHOLD
            }
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )
    
    def search_similar_documents(self, query: str, k: int = 5) -> List[Tuple[Document, float]]:
        """Recherche des documents similaires avec scores"""
        if not self.vectorstore:
            return []
        
        try:
            results = self.vectorstore.similarity_search_with_score(query, k=k)
            return results
        except Exception as e:
            st.error(f"Erreur lors de la recherche: {e}")
            return []
    
    def ask_question(self, question: str, use_history: bool = False) -> Dict:
        """Pose une question et retourne la réponse avec métadonnées"""
        if not self.vectorstore:
            if not self.load_vectorstore():
                return {
                    "answer": "Erreur: Aucun document indexé. Veuillez d'abord indexer des documents.",
                    "sources": [],
                    "confidence": 0.0
                }
        
        if not self.qa_chain:
            self.setup_qa_chain(use_history)
        
        try:
            # Obtenir la réponse
            if use_history:
                history_text = "\n".join([
                    f"Q: {item['question']}\nR: {item['answer']}" 
                    for item in self.conversation_history[-3:]
                ])
                
                result = self.qa_chain({
                    "query": question,
                    "history": history_text
                })
            else:
                result = self.qa_chain({"query": question})
            
            # Extraire les sources
            sources = []
            if "source_documents" in result:
                for doc in result["source_documents"]:
                    sources.append({
                        "content": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content,
                        "source": doc.metadata.get("source_file", "Source inconnue"),
                        "file_type": doc.metadata.get("file_type", ""),
                        "chunk_id": doc.metadata.get("chunk_id", "")
                    })
            
            # Calculer un score de confiance basique
            confidence = min(len(sources) / MAX_RESULTS, 1.0)
            
            # Sauvegarder dans l'historique
            self.conversation_history.append({
                "question": question,
                "answer": result["result"],
                "sources": sources,
                "confidence": confidence
            })
            
            # Limiter la taille de l'historique
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]
            
            return {
                "answer": result["result"],
                "sources": sources,
                "confidence": confidence
            }
            
        except Exception as e:
            st.error(f"Erreur lors de la génération de la réponse: {e}")
            return {
                "answer": f"Erreur lors de la génération de la réponse: {e}",
                "sources": [],
                "confidence": 0.0
            }
    
    def get_vectorstore_stats(self) -> Dict:
        """Retourne des statistiques sur le vectorstore"""
        if not self.vectorstore:
            return {}
        
        try:
            # Nombre total de documents
            total_docs = self.vectorstore.index.ntotal
            
            return {
                "total_documents": total_docs,
                "embedding_dimension": self.vectorstore.index.d if hasattr(self.vectorstore.index, 'd') else "N/A"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def clear_history(self):
        """Efface l'historique de conversation"""
        self.conversation_history = []
    
    def export_conversation(self) -> str:
        """Exporte la conversation en format markdown"""
        if not self.conversation_history:
            return "Aucune conversation à exporter."
        
        markdown = "# Historique de conversation\n\n"
        
        for i, item in enumerate(self.conversation_history, 1):
            markdown += f"## Question {i}\n"
            markdown += f"**Q:** {item['question']}\n\n"
            markdown += f"**R:** {item['answer']}\n\n"
            
            if item['sources']:
                markdown += "**Sources:**\n"
                for j, source in enumerate(item['sources'], 1):
                    markdown += f"{j}. {source['source']} ({source['file_type']})\n"
                markdown += "\n"
            
            markdown += f"**Confiance:** {item['confidence']:.2f}\n\n"
            markdown += "---\n\n"
        
        return markdown

# Instance globale pour la session
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = AdvancedQAChain()

def get_qa_chain() -> AdvancedQAChain:
    """Retourne l'instance QA Chain"""
    return st.session_state.qa_chain

def ask_question(question: str, use_history: bool = False) -> Dict:
    """Fonction simplifiée pour poser une question"""
    qa_chain = get_qa_chain()
    return qa_chain.ask_question(question, use_history)