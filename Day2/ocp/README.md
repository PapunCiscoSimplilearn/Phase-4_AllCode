# Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification. New functionality should be added without unnecessarily changing existing, tested code.

## Payment example

A payment processor that uses an `if` or `elif` branch for every payment type must be modified each time a new type is added. Those changes can affect existing payment methods.

Here, `PaymentMethod` defines the `pay(amount)` interface, and each payment class implements it. `PaymentProcessor` calls that interface without knowing the specific payment type. To support another method, create a new `PaymentMethod` subclass; the processor does not need to change.

This makes extensions easier to add and reduces the risk of breaking existing processing logic. The example only prints messages; it does not perform real transactions.

Run the example from the workspace root:

```bash
python3 Day2/ocp/main.py
```

Expected output:

```text
Credit card payment: 1000
Debit card payment: 1500
UPI payment: 2000
PayPal payment: 3000
Net banking payment: 4000
```