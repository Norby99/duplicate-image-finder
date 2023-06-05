from abc import ABC, abstractmethod
from libraries.view.scenes.abstract_scene import AbstractScene
from libraries.model.abstract_model import AbstractModel

from typing import Any

class AbstractController(ABC):

    @abstractmethod
    def _set_model(self, model: Any) -> None:
        pass

    @abstractmethod
    def _set_scene(self, scene: Any) -> None:
        pass

    @abstractmethod
    def get_model(self) -> Any:
        pass

    @abstractmethod
    def get_scene(self) -> Any:
        pass

    @abstractmethod
    def tick(self) -> bool:
        pass
