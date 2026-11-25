# Practical Workshop: E-Commerce Order Management

## Business Requirements

An online shopping application should let customers register and log in, browse products, add products to a cart, place and track orders, make payments, receive email notifications, cancel orders, and request refunds.

The initial design includes `UserManager` for registration and authentication, `ProductManager` for product management and search, `OrderManager` for orders, `PaymentManager` for payments, `InventoryManager` for stock, `NotificationManager` for email and SMS, and `DatabaseManager` for database operations.

## Initial Design

The following implementation mixes several responsibilities in `OrderManager`:

```python
class OrderManager:
    def __init__(self):
        self.db = MySQLDatabase()

    def create_order(self, customer, product, quantity):
        if product.stock >= quantity:
            amount = product.price * quantity

            if customer.payment_type == "UPI":
                print("Processing UPI payment")
            elif customer.payment_type == "CARD":
                print("Processing Card payment")

            product.stock -= quantity
            self.db.save_order(customer, product, quantity)
            print("Sending order confirmation email")
            return "Order placed successfully"

        return "Insufficient stock"


class MySQLDatabase:
    def save_order(self, customer, product, quantity):
        print("Saving order into MySQL database")
```

Order, payment, inventory, and email behavior are mixed, making them difficult to test independently. The conditional payment selection makes extension harder, and directly constructing `MySQLDatabase` tightly couples order management to MySQL.

## SOLID Evaluation

| Principle | Evaluation | Reason |
| --- | --- | --- |
| SRP | Violated | `OrderManager` handles orders, payments, inventory, and notifications. |
| OCP | Violated | Adding a payment method requires changing the payment conditional in `OrderManager`. |
| LSP | Needs review | Payment implementations must honor their abstraction's contract, but no relevant hierarchy is shown. |
| ISP | Needs review | No relevant interfaces are shown, so we cannot determine whether implementations are forced to provide unrelated operations. |
| DIP | Violated | `OrderManager` directly creates a concrete `MySQLDatabase`. |

LSP and ISP cannot be conclusively evaluated from this limited code; do not mark a principle violated without sufficient evidence.

## SOLID Redesign

The proposed design separates `OrderService` (orders), `PaymentService` (payment processing), `PaymentMethod` (payment abstraction), `InventoryService` (stock), `NotificationService` (notifications), `OrderRepository` (order persistence), and `Database` (database abstraction).

The simplified implementation separates each component into its own file:

- [main.py](main.py): creates the dependencies and runs the example.
- [order_service.py](order_service.py): coordinates order placement.
- [payment_method.py](payment_method.py): defines the payment abstraction and payment methods.
- [inventory_service.py](inventory_service.py): checks and updates stock.
- [notification_service.py](notification_service.py): sends order confirmations.
- [order_repository.py](order_repository.py): defines the order repository abstraction and the example MySQL repository.

The order service receives its dependencies through its constructor. It calls the payment method directly rather than adding a separate payment service or database abstraction. The `MySQLOrderRepository` is only a print-based example; it does not connect to MySQL.

| Principle | Demonstration |
| --- | --- |
| SRP | Payment, inventory, notification, and order responsibilities are separated. |
| OCP | New payment implementations can be supplied without modifying `OrderService`. |
| LSP | Each payment implementation follows the `PaymentMethod.pay(amount)` contract. |
| ISP | The payment and repository interfaces are small and focused. |
| DIP | `OrderService` receives its dependencies through its constructor instead of constructing them. |

Run the example from the workspace root:

```bash
python3 Day2/ecommerce_order_management/main.py
```

Expected output:

```text
UPI payment successful: 100000
Inventory updated
Order saved into MySQL
Order confirmation sent to Irfan
Order placed successfully
```

This example demonstrates order placement only; it does not implement the full shopping application. A production implementation would additionally need transaction management, payment failure handling, stock reservation, rollback, and idempotency.