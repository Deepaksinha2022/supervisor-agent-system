class CitationEvaluator:

    def evaluate(
        self,
        answer
    ):

        citation_patterns = [
            "[Source]",
            "(Source)",
            "[Citation]",
            "(Citation)"
        ]

        has_citation = any(
            pattern in answer
            for pattern in citation_patterns
        )

        return {
            "citation_present":
                has_citation
        }