from backend.app.evaluation.hallucination_evaluator import (
    HallucinationEvaluator
)

from backend.app.evaluation.citation_evaluator import (
    CitationEvaluator
)

hallucination = (
    HallucinationEvaluator()
)

citation = (
    CitationEvaluator()
)

ground_truth = (
    "Redis is an in-memory database"
)

generated_answer = (
    "Redis is an in-memory database used for caching"
)

answer_with_citation = (
    "Redis is used for caching [Source]"
)

print(
    hallucination.evaluate(
        ground_truth,
        generated_answer
    )
)

print()

print(
    citation.evaluate(
        answer_with_citation
    )
)