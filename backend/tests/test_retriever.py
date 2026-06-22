import asyncio

from app.rag.retriever import retrieve


async def main():

    results = await retrieve(
        "What is Redis?"
    )

    print(results)


asyncio.run(main())