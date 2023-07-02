from typing import Callable, Any

class Observable(object):
    """ Observer pattern implementation
        You can implement this class in 2 ways:
        1. Inherit from this class and call the subscribe-fire method
        2. Create an instance of this class and call the subscribe-fire method
    """

    __callback: Callable

    def __init__(self, function: Callable) -> None:
        self.__callback = function

    def subscribe(self, callback: Callable) -> None:
        self.__callback = callback

    def fire(self, **attrs: Any) -> None:
        self.__callback(**attrs)
