from abc import ABCMeta, abstractmethod

class ModelInterface:
    __metaclass__ = ABCMeta
    @abstractmethod
    def ask(self, product_id: int, k: int = 5) -> int:
        raise Exception('not implemented')