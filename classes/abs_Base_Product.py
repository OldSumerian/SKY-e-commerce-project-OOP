from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def about_product(self):
        pass
