class Iterator:

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.current = None

    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            self.current = next(self.iterator)
        except StopIteration:
            self.current = None
        finally:
            return self.current
