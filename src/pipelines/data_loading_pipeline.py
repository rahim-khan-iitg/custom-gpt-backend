from components.data_ingestion import DataIngestion
from components.db_loader import load_to_qdrant,load_to_chroma
from utils.utils import load_embedding_model
from utils.utils import connect_to_chroma_as_retriver

if __name__=="__main__":
    x=load_embedding_model()
    r=connect_to_chroma_as_retriver()
    print(str(r))
    data_object=DataIngestion()
    texts=data_object.initialize_data_ingestion()
    db_choice=input("chroma/qdrant ").strip()
    if db_choice=="qdrant":
        collection_name=input("write the qdrant collection name ")
        loader_object=load_to_qdrant(collection_name)
        loader_object.initialize_upload(texts)
    elif db_choice=="chroma":
        loader_object=load_to_chroma()
        loader_object.initialize_upload(texts)
