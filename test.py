from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class Test:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, result=None):
        raise NotImplementedError(NOT_IMPLEMENTED)
