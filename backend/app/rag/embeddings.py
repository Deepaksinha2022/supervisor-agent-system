from sentence_transformers import SentenceTransformer

import asyncio

model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(texts):

    
    embeddings = model.encode(texts)

    return embeddings

async def generate_embeddings_async(
    texts
):

    loop = asyncio.get_event_loop()

    embeddings = await loop.run_in_executor(
        None,
        model.encode,
        texts
    )

    return embeddings