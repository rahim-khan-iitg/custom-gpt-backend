from utils.logger import logging
from utils.exceptions import CustomException
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
import os,sys

from chromadb.config import Settings
import chromadb
from langchain.vectorstores import Chroma

CHROMA_SETTINGS = Settings(persist_directory="./",anonymized_telemetry=False)

load_dotenv(".env")
HUGGINGFACE_EMBEDDING_REPO_ID=os.environ.get("HUGGINGFACE_EMBEDDING_REPO_ID")
HUGGINGFACE_LLM_REPO_ID=os.environ.get("HUGGINGFACE_LLM_REPO_ID")
HUGGINGFACE_API_TOKEN=os.environ.get("HUGGINGFACE_API_TOKEN")
QDRANT_URL=os.environ.get("QDRANT_URL")
QDRANT_API_KEY=os.environ.get("QDRANT_API_KEY")

def load_embedding_model():
    try:
        logging.info("loading embedding model")
        print(HUGGINGFACE_EMBEDDING_REPO_ID)
        # embedding_model=HuggingFaceEmbeddings(model_name=HUGGINGFACE_EMBEDDING_REPO_ID) # this model downloads the binary file locally
        embedding_model=HuggingFaceInferenceAPIEmbeddings(api_key=HUGGINGFACE_API_TOKEN,model_name=HUGGINGFACE_EMBEDDING_REPO_ID)
        logging.info("model successfully loaded")
        return embedding_model
        
    except Exception as e:
        logging.info("model not loaded properly")
        raise CustomException(sys,e)
    

def load_LLM():
    try:
        logging.info("connecting to chat model")
        llm = HuggingFaceHub(repo_id=HUGGINGFACE_LLM_REPO_ID, model_kwargs={"temperature": 0.5, "max_length": 64},huggingfacehub_api_token=HUGGINGFACE_API_TOKEN)
        logging.info("LLM connected successfully")
        return llm
    except Exception as e:
        logging("LLM not connected")
        raise CustomException(sys,e)

def connect_to_qdrant_as_retriver():
    client=QdrantClient(QDRANT_URL,api_key=QDRANT_API_KEY)
    collection_name="big_basket"
    embedding_model=load_embedding_model()
    qdrant=Qdrant(client=client,collection_name=collection_name,embeddings=embedding_model)
    retriver=qdrant.as_retriever()
    return retriver

def connect_to_chroma_as_retriver():
    embedding_model=load_embedding_model()
    chroma_client = chromadb.PersistentClient(settings=CHROMA_SETTINGS , path="./")
    db = Chroma(persist_directory="./", embedding_function=embedding_model, client_settings=CHROMA_SETTINGS, client=chroma_client)
    retriever=db.as_retriever()
    return retriever