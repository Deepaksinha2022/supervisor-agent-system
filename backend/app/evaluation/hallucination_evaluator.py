class HallucinationEvaluator:

    def evaluate(
        self,
        ground_truth,
        generated_answer
    ):

        ground_truth_words = set(
            ground_truth.lower().split()
        )

        generated_words = set(
            generated_answer.lower().split()
        )

        overlap = len(
            ground_truth_words.intersection(
                generated_words
            )
        )

        score = (
            overlap
            / len(
                ground_truth_words
            )
        )

        return {
            "hallucination_score":
                round(score, 2)
        }