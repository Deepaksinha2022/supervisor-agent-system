from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    async def execute(
        self,
        task
    ):
        pass

    @property
    def agent_name(self):
        return self.__class__.__name__
    
    @property
    def capabilities(self):
        return []