from sentence_transformers import (
    CrossEncoder
)

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank(
    query,
    documents
):

    pairs = []

    for doc in documents:

        pairs.append(
            [query, doc]
        )

    scores = model.predict(
        pairs
    )

    ranked = sorted(

        zip(
            documents,
            scores
        ),

        key=lambda x: x[1],

        reverse=True
    )

    return ranked