class Observable(object):

    __callbacks: list = []


    def subscribe(self, callback):
        self.__callbacks.append(callback)

    def fire(self, **attrs):
        for fn in self.__callbacks:
            fn(**attrs)
