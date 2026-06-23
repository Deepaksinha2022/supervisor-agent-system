from backend.app.models.complexity_classifier import (
    ComplexityClassifier
)


class ModelRouter:

    def __init__(
        self,
        registry
    ):

        self.registry = registry

        self.classifier = (
            ComplexityClassifier()
        )

    def route(
        self,
        task
    ):

        complexity = (
            self.classifier.classify(
                task
            )
        )

        if complexity == "simple":

            return self.registry.get(
                "small_model"
            )

        if complexity == "medium":

            return self.registry.get(
                "medium_model"
            )

        return self.registry.get(
            "large_model"
        )