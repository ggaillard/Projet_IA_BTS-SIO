import streamlit as st
from app.ingest import ingest
from app.qa_chain import ask_question

st.title("🤖 Chatbot - Base documentaire")
if st.button("Indexer les documents"):
    ingest()
    st.success("Indexation terminée ✅")

question = st.text_input("Posez votre question :")
if question:
    answer = ask_question(question)
    st.markdown(f"**Réponse :** {answer}")
