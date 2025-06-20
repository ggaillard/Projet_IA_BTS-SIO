from git import Repo
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.config import REPO_URL
import os

def ingest():
    if os.path.exists("data") and os.listdir("data"):
        print("Documents déjà présents")
    else:
        Repo.clone_from(REPO_URL, "data")
    texts = []
    for root, _, files in os.walk("data"):
        for fname in files:
            path = os.path.join(root, fname)
            loader = TextLoader(path, encoding="utf-8")
            texts.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, overlap=200)
    docs = splitter.split_documents(texts)
    embeddings = OpenAIEmbeddings()
    store = FAISS.from_documents(docs, embeddings)
    store.save_local("vectorstore")
