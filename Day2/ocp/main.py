from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Credit card payment: {amount}")


class DebitCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Debit card payment: {amount}")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"UPI payment: {amount}")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"PayPal payment: {amount}")


class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Net banking payment: {amount}")


class PaymentProcessor:
    def process(self, payment_method, amount):
        payment_method.pay(amount)


def main():
    processor = PaymentProcessor()
    processor.process(CreditCardPayment(), 1000)
    processor.process(DebitCardPayment(), 1500)
    processor.process(UPIPayment(), 2000)
    processor.process(PayPalPayment(), 3000)
    processor.process(NetBankingPayment(), 4000)


if __name__ == "__main__":
    main()