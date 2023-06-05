from typing import TypeVar, Any

T = TypeVar('T', bound='Iterator')

class Iterator:

    def __init__(self: T, iterator: Any) -> None:
        self.iterator = iter(iterator)
        self.current = None

    def __iter__(self: T) -> T:
        return self
        
    def __next__(self: T) -> Any:
        try:
            self.current = next(self.iterator)
        except StopIteration:
            self.current = None
        finally:
            return self.current
        
    def next(self: T) -> Any:
        return self.__next__()
