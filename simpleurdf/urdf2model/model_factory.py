from abc import ABC, abstractmethod

from .metamodel import IModel


class UrdfFactory(ABC):
    @abstractmethod
    def buildModel(self) -> IModel:
        pass
