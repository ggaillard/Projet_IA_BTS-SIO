# app/main.py

import os
import sys

# 👇 Ajout du chemin racine au path Python (fonctionne partout)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.ingest import ingest
from app.qa_chain import create_qa_chain

st.set_page_config(page_title="Chatbot IA avec base documentaire", layout="wide")
st.title("📚 Chatbot IA - Base documentaire")

if st.button("Indexer les documents"):
    ingest()
    st.success("Indexation terminée ✅")

query = st.text_input("Pose ta question à l'IA 👇")

if query:
    response = create_qa_chain()(query)
    st.markdown("**Réponse :**")
    st.write(response)
