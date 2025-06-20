from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.config import MODEL_NAME, PROVIDER, MISTRAL_API_KEY, MISTRAL_API_BASE

def ask_question(query: str) -> str:
    store = FAISS.load_local("vectorstore", OpenAIEmbeddings())

    if PROVIDER == "mistral":
        llm = ChatOpenAI(
            base_url=MISTRAL_API_BASE,
            api_key=MISTRAL_API_KEY,
            model_name=MODEL_NAME
        )
    else:
        from langchain.llms import OpenAI
        llm = OpenAI(model_name=MODEL_NAME)

    from langchain.chains import RetrievalQA
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=store.as_retriever())
    return qa.run(query)
