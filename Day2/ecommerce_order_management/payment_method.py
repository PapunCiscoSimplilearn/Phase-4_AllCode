from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"UPI payment successful: {amount}")


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Card payment successful: {amount}")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"PayPal payment successful: {amount}")