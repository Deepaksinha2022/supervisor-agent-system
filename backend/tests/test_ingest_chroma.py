from app.rag.embeddings import (
    generate_embeddings
)

from app.rag.vector_store import (
    store_chunks
)


class DummyChunk:

    def __init__(
        self,
        text,
        chunk_id
    ):
        self.page_content = text

        self.metadata = {
            "chunk_id": chunk_id
        }


chunks = [
    DummyChunk(
        "Redis is an in-memory key-value database used for caching, session storage and workflow state management.",0
    ),
    DummyChunk(
        "Redis provides very fast read and write operations because data is stored in memory.",1
    ),
    DummyChunk(
        "Redis supports strings, hashes, lists, sets and sorted sets.",2
    )
]

embeddings = generate_embeddings(
    [
        chunk.page_content
        for chunk in chunks
    ]
)

store_chunks(
    chunks,
    embeddings
)

print("Documents stored")