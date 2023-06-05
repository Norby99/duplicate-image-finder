from typing import Callable, Any

class Observable(object):

    __callbacks: list = []

    def subscribe(self, callback: Callable) -> None:
        self.__callbacks.append(callback)

    def fire(self, **attrs: Any) -> None:
        for fn in self.__callbacks:
            fn(**attrs)
