class ComplexityClassifier:

    def classify(
        self,
        task
    ):

        task = task.lower()

        if len(task.split()) <= 3:

            return "simple"

        if any(
            word in task
            for word in [
                "compare",
                "analysis",
                "evaluate"
            ]
        ):

            return "medium"

        return "complex"