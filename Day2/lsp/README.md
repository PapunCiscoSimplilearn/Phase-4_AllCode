# Liskov Substitution Principle (LSP)

Objects of a child class should be usable wherever objects of the parent class are expected without changing the correctness of the application. A subclass must honor the behavior promised by its parent.

## Bird example

If every `Bird` promises a `fly()` method, a `Penguin` that raises an exception when asked to fly violates that promise. Code expecting a bird that can fly cannot safely use a penguin.

Here, `Bird` only promises behavior shared by both birds. `FlyingBird` adds `fly()`, `Sparrow` implements it, and `Penguin` provides its own `swim()` method. Both can be used as birds, while only flying birds are passed to `make_bird_fly`.

This makes inheritance and polymorphism more predictable and reduces unexpected runtime errors. Similarly, a payment application should only treat payment methods that genuinely support refunds as refundable payments.

Run the example from the workspace root:

```bash
python3 Day2/lsp/main.py
```

Expected output:

```text
Bird is eating
Bird is eating
Sparrow is flying
Penguin is swimming
```