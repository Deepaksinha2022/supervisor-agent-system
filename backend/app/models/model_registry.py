class ModelRegistry:

    def __init__(self):

        self.models = {}

    def register(
        self,
        name,
        metadata
    ):

        self.models[name] = metadata

    def get(
        self,
        name
    ):

        return self.models.get(
            name
        )

    def list_models(
        self
    ):

        return list(
            self.models.keys()
        )