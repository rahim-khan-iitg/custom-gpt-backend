from components.data_ingestion import DataIngestion
from components.db_loader import load_to_qdrant

if __name__=="__main__":
    data_object=DataIngestion()
    texts=data_object.initialize_data_ingestion()
    collection_name=input("write the qdrant collection name ")
    loader_object=load_to_qdrant(collection_name)
    loader_object.initialize_upload(texts)