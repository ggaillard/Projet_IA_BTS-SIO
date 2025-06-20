import os
import sys
import json
from datetime import datetime

# Ajout du chemin racine au path Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.ingest import ingest_documents
from app.qa_chain import get_qa_chain, ask_question
from app.config import validate_config, PROVIDER, MODEL_NAME

# Configuration de la page
st.set_page_config(
    page_title="Chatbot IA - Base documentaire",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        padding: 1rem 0;
        border-bottom: 2px solid #f0f0f0;
        margin-bottom: 2rem;
    }
    .source-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #007bff;
        margin: 0.5rem 0;
    }
    .confidence-high { color: #28a745; }
    .confidence-medium { color: #ffc107; }
    .confidence-low { color: #dc3545; }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f1f8e9;
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # En-tête principal
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("📚 Chatbot IA - Base documentaire")
    st.markdown("*Assistant intelligent pour l'analyse de documents*")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Validation de la configuration
    config_errors = validate_config()
    if config_errors:
        st.error("Erreurs de configuration:")
        for error in config_errors:
            st.error(f"• {error}")
        st.stop()
    
    # Sidebar pour la configuration et les outils
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.info(f"**Provider:** {PROVIDER}")
        st.info(f"**Modèle:** {MODEL_NAME}")
        
        st.header("📁 Gestion des documents")
        
        # Onglets pour les différentes sources
        tab1, tab2, tab3 = st.tabs(["Repository", "Upload", "Statistiques"])
        
        with tab1:
            st.subheader("Repository Git")
            repo_url = st.text_input(
                "URL du repository:",
                placeholder="https://github.com/user/repo.git"
            )
            
            if st.button("📥 Cloner et indexer", key="clone_repo"):
                if repo_url:
                    with st.spinner("Clonage et indexation en cours..."):
                        success = ingest_documents(repo_url=repo_url)
                    if success:
                        st.success("✅ Repository indexé avec succès!")
                        st.rerun()
                else:
                    st.warning("Veuillez entrer une URL de repository")
        
        with tab2:
            st.subheader("Upload de fichiers")
            uploaded_files = st.file_uploader(
                "Choisir des fichiers",
                accept_multiple_files=True,
                type=['txt', 'md', 'py', 'js', 'html', 'css', 'json', 'xml', 'pdf']
            )
            
            if uploaded_files:
                st.write(f"**{len(uploaded_files)} fichier(s) sélectionné(s):**")
                for file in uploaded_files:
                    st.write(f"• {file.name} ({file.size} bytes)")
                
                if st.button("📤 Uploader et indexer", key="upload_files"):
                    with st.spinner("Upload et indexation en cours..."):
                        success = ingest_documents(uploaded_files=uploaded_files)
                    if success:
                        st.success("✅ Fichiers indexés avec succès!")
                        st.rerun()
        
        with tab3:
            st.subheader("Statistiques")
            qa_chain = get_qa_chain()
            stats = qa_chain.get_vectorstore_stats()
            
            if stats:
                if "error" in stats:
                    st.error(f"Erreur: {stats['error']}")
                else:
                    st.metric("Documents indexés", stats.get("total_documents", "N/A"))
                    st.metric("Dimension des embeddings", stats.get("embedding_dimension", "N/A"))
            else:
                st.info("Aucune statistique disponible")
            
            # Bouton pour effacer l'historique
            if st.button("🗑️ Effacer l'historique"):
                qa_chain.clear_history()
                if 'messages' in st.session_state:
                    st.session_state.messages = []
                st.success("Historique effacé!")
                st.rerun()
    
    # Interface principale
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("💬 Conversation")
        
        # Options de conversation
        use_history = st.checkbox("Utiliser l'historique de conversation", value=True)
        
        # Initialiser l'historique des messages
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Afficher l'historique des messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # Afficher les sources pour les réponses de l'assistant
                if message["role"] == "assistant" and "sources" in message:
                    if message["sources"]:
                        with st.expander("📋 Sources utilisées"):
                            for i, source in enumerate(message["sources"], 1):
                                st.markdown(f"""
                                <div class="source-box">
                                    <strong>Source {i}:</strong> {source['source']}<br>
                                    <strong>Type:</strong> {source['file_type']}<br>
                                    <strong>Extrait:</strong> {source['content']}
                                </div>
                                """, unsafe_allow_html=True)
                    
                    # Afficher le score de confiance
                    if "confidence" in message:
                        confidence = message["confidence"]
                        if confidence >= 0.7:
                            conf_class = "confidence-high"
                            conf_text = "Élevée"
                        elif confidence >= 0.4:
                            conf_class = "confidence-medium"
                            conf_text = "Moyenne"
                        else:
                            conf_class = "confidence-low"
                            conf_text = "Faible"
                        
                        st.markdown(f'<p><strong>Confiance:</strong> <span class="{conf_class}">{conf_text} ({confidence:.2f})</span></p>', unsafe_allow_html=True)
        
        # Zone de saisie pour nouvelle question
        if prompt := st.chat_input("Posez votre question..."):
            # Ajouter le message utilisateur à l'historique
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Afficher le message utilisateur
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Générer la réponse
            with st.chat_message("assistant"):
                with st.spinner("Recherche en cours..."):
                    response = ask_question(prompt, use_history=use_history)
                
                # Afficher la réponse
                st.markdown(response["answer"])
                
                # Afficher les sources si disponibles
                if response["sources"]:
                    with st.expander("📋 Sources utilisées"):
                        for i, source in enumerate(response["sources"], 1):
                            st.markdown(f"""
                            <div class="source-box">
                                <strong>Source {i}:</strong> {source['source']}<br>
                                <strong>Type:</strong> {source['file_type']}<br>
                                <strong>Extrait:</strong> {source['content']}
                            </div>
                            """, unsafe_allow_html=True)
                
                # Afficher le score de confiance
                confidence = response["confidence"]
                if confidence >= 0.7:
                    conf_class = "confidence-high"
                    conf_text = "Élevée"
                elif confidence >= 0.4:
                    conf_class = "confidence-medium"
                    conf_text = "Moyenne"
                else:
                    conf_class = "confidence-low"
                    conf_text = "Faible"
                
                st.markdown(f'<p><strong>Confiance:</strong> <span class="{conf_class}">{conf_text} ({confidence:.2f})</span></p>', unsafe_allow_html=True)
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response["answer"],
                "sources": response["sources"],
                "confidence": response["confidence"]
            })
    
    with col2:
        st.header("🔍 Outils d'analyse")
        
        # Recherche de documents similaires
        st.subheader("Recherche de documents")
        search_query = st.text_input("Rechercher dans les documents:")
        
        if search_query:
            qa_chain = get_qa_chain()
            if qa_chain.load_vectorstore():
                similar_docs = qa_chain.search_similar_documents(search_query, k=3)
                
                if similar_docs:
                    st.write(f"**{len(similar_docs)} document(s) trouvé(s):**")
                    
                    for i, (doc, score) in enumerate(similar_docs, 1):
                        with st.expander(f"Document {i} (Score: {score:.3f})"):
                            st.write(f"**Source:** {doc.metadata.get('source_file', 'Inconnue')}")
                            st.write(f"**Type:** {doc.metadata.get('file_type', 'Inconnu')}")
                            st.write(f"**Contenu:** {doc.page_content[:300]}...")
                else:
                    st.info("Aucun document trouvé")
            else:
                st.warning("Aucun document indexé")
        
        # Exemples de questions
        st.subheader("💡 Questions suggérées")
        example_questions = [
            "Quel est l'objectif de ce projet ?",
            "Comment installer les dépendances ?",
            "Quelles sont les étapes d'utilisation ?",
            "Quels fichiers sont importants ?",
            "Comment lancer l'application ?"
        ]
        
        for question in example_questions:
            if st.button(question, key=f"example_{hash(question)}"):
                st.session_state.example_question = question
                st.rerun()
        
        # Si une question d'exemple a été sélectionnée
        if hasattr(st.session_state, 'example_question'):
            prompt = st.session_state.example_question
            del st.session_state.example_question
            
            # Traiter la question d'exemple comme une nouvelle question
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            with st.spinner("Traitement de la question..."):
                response = ask_question(prompt, use_history=use_history)
            
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response["answer"],
                "sources": response["sources"],
                "confidence": response["confidence"]
            })
            
            st.rerun()
        
        # Export de la conversation
        st.subheader("📄 Export")
        qa_chain = get_qa_chain()
        
        if st.button("📋 Exporter la conversation"):
            conversation_md = qa_chain.export_conversation()
            
            if conversation_md != "Aucune conversation à exporter.":
                st.download_button(
                    label="💾 Télécharger (Markdown)",
                    data=conversation_md,
                    file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            else:
                st.info("Aucune conversation à exporter")
        
        # Statistiques de la session
        st.subheader("📊 Session actuelle")
        if st.session_state.messages:
            user_messages = [msg for msg in st.session_state.messages if msg["role"] == "user"]
            assistant_messages = [msg for msg in st.session_state.messages if msg["role"] == "assistant"]
            
            st.metric("Questions posées", len(user_messages))
            st.metric("Réponses générées", len(assistant_messages))
            
            if assistant_messages:
                avg_confidence = sum(msg.get("confidence", 0) for msg in assistant_messages) / len(assistant_messages)
                st.metric("Confiance moyenne", f"{avg_confidence:.2f}")
        else:
            st.info("Aucune interaction pour le moment")

if __name__ == "__main__":
    main()