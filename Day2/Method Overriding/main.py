class Payment:
    def process_payment(self):
        print("Processing payment")


class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing Credit Card Payment")

    def display(self):
        print("display")


class UPIPayment(Payment):
    def process_payment(self):
        print("Processing UPI Payment")


class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal Payment")


class PaymentWithValidation:
    def process_payment(self):
        print("Common payment validation")


class ValidatedUPIPayment(PaymentWithValidation):
    def process_payment(self):
        super().process_payment()
        print("Processing UPI payment")


def main():
    credit = CreditCardPayment()
    upi = UPIPayment()
    paypal = PayPalPayment()

    credit.process_payment()
    credit.display()
    upi.process_payment()
    paypal.process_payment()

    print("\nCalling the parent method with super():")
    validated_upi = ValidatedUPIPayment()
    validated_upi.process_payment()


if __name__ == "__main__":
    main()