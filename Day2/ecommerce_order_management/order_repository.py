from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass


class MySQLOrderRepository(OrderRepository):
    def save(self, order):
        print("Order saved into MySQL")