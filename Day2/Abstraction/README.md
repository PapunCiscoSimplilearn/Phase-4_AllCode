# Abstraction in Python

Abstraction exposes the essential operations of an object while hiding implementation details. It helps standardize behavior, reduce coupling, improve maintainability, and separate an interface from its implementations.

Python's `abc` module supports abstraction:

- `ABC` is the base class for an abstract class.
- `@abstractmethod` marks an operation that concrete child classes must implement.

## Payment example

`Payment` declares `process_payment(amount)` without defining payment-specific behavior. `CreditCardPayment` and `UPIPayment` each implement that method in their own way. Since both implement the abstract method, their objects can be created and used normally.

Run the example from the workspace root:

```bash
python3 Day2/Abstraction/main.py
```

Expected payment output:

```text
Processing Credit Card payment: 5000
Processing UPI payment: 2000
```

The script also attempts to instantiate `Payment` and catches the resulting `TypeError`. An abstract class with unimplemented abstract methods cannot be instantiated; the exact error wording can vary slightly by Python version.

The `super().processPayment()` line in the prompt should not be used here. The method is named `process_payment` (not `processPayment`), and the abstract parent method only contains `pass`, so there is no payment behavior to reuse. The child classes should implement the required method directly.