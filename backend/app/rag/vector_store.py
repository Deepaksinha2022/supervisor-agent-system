import chromadb


client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="enterprise_rag"
)

def store_chunks(chunks, embeddings):

    ids = []

    documents = []

    metadatas = []

    for chunk in chunks:

        ids.append(
            str(
                chunk.metadata["chunk_id"]
            )
        )

        documents.append(
            chunk.page_content
        )

        metadatas.append(
            chunk.metadata
        )

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas
    )


def search_chunks(
    query_embedding,
    k=3,department=None
):
    if department:
        results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k,where={"department":department}
    )
    else:
      results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=k
    )  
    return results