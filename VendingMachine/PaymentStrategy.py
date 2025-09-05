from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def paymentwithintention(self, amount):
        pass

