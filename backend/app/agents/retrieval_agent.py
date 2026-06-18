import chromadb

from langsmith import traceable

class RetrievalAgent:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

    @traceable
    def get_collection(self, collection_name: str):

        return self.client.get_or_create_collection(
            name=collection_name
        )