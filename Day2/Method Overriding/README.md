# Method Overriding in Python

Method overriding happens when a child class defines a method with the same name as one in its parent. Calling that method on a child object runs the child's implementation, allowing it to customize inherited behavior.

## Payment example

`Payment` defines `process_payment()`. `CreditCardPayment`, `UPIPayment`, and `PayPalPayment` inherit from it and each override `process_payment()` with payment-specific behavior. `CreditCardPayment` also defines its own `display()` method.

The objects use the overridden method like any other method:

```python
credit.process_payment()
upi.process_payment()
paypal.process_payment()
```

Each call runs the implementation belonging to that object's class.

## Inheritance and overriding

| Inheritance | Method overriding |
| --- | --- |
| A child class acquires properties and methods from a parent. | A child class replaces an inherited method with its own implementation. |
| Promotes code reuse. | Customizes inherited behavior. |
| Establishes a parent-child relationship. | Requires inheritance and a matching method name. |
| A child can use inherited methods as-is. | A child can provide a different implementation. |

## Calling the parent method

An overridden method can call its parent's implementation with `super()`. The example in `main.py` prints:

```text
Common payment validation
Processing UPI payment
```

An abstract parent does not categorically prevent `super()` calls in Python. If an abstract method contains an implementation, a child can call it with `super()` after overriding the method. If the parent method has no usable implementation (for example, it raises `NotImplementedError`), calling it will not provide useful behavior.

## Run the example

From the workspace root, run:

```bash
python3 "Day2/Method Overriding/main.py"
```

The first payment calls print:

```text
Processing Credit Card Payment
display
Processing UPI Payment
Processing PayPal Payment
```

`display` appears because the sample calls `credit.display()`, although it was omitted from the expected output in the prompt.