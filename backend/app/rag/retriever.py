from backend.app.rag.embeddings import (
    generate_embeddings
)

from backend.app.rag.vector_store import (
    search_chunks
)


async def retrieve(
    query,
    k=3,
    department=None
):

    query_embedding = generate_embeddings(
        [query]
    )[0]

    results = search_chunks(
        query_embedding,
        k,
        department
    )

    return results