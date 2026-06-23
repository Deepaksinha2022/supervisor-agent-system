from abc import ABC, abstractmethod


class BaseTool(ABC):

    @property
    def tool_name(self):
        return self.__class__.__name__

    @abstractmethod
    async def execute(
        self,
        *args,
        **kwargs
    ):
        pass

    @property
    def capabilities(
        self
    ):
        return []