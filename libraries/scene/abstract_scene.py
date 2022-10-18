from abc import ABC, abstractmethod

class AbstractScene(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def destroy(self):
        pass
