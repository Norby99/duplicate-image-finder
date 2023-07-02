from typing import Callable, Any

class Observable(object):

    __callbacks: list = []

    def __init__(self, functions: list[Callable] = []) -> None:
        self.__callbacks = functions

    def subscribe(self, callback: Callable) -> None:
        self.__callbacks.append(callback)

    def fire(self, **attrs: Any) -> None:
        for fn in self.__callbacks:
            fn(**attrs)

    def unsubscribe(self) -> None:
        self.__callbacks.clear()
