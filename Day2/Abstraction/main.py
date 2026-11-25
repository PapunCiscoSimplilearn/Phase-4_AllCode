from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment: {amount}")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment: {amount}")


def main():
    credit = CreditCardPayment()
    credit.process_payment(5000)

    upi = UPIPayment()
    upi.process_payment(2000)

    try:
        Payment()
    except TypeError as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()