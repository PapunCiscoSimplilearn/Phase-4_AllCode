class OrderService:
    def __init__(
        self,
        payment_method,
        inventory_service,
        notification_service,
        order_repository
    ):
        self.payment_method = payment_method
        self.inventory_service = inventory_service
        self.notification_service = notification_service
        self.order_repository = order_repository

    def create_order(self, customer, product, quantity):
        if not self.inventory_service.check_stock(
            product, quantity
        ):
            return "Insufficient stock"

        amount = product["price"] * quantity

        self.payment_method.pay(amount)

        self.inventory_service.reduce_stock(
            product, quantity
        )

        order = {
            "customer": customer,
            "product": product["name"],
            "quantity": quantity,
            "amount": amount
        }

        self.order_repository.save(order)

        self.notification_service.send_order_confirmation(
            customer
        )

        return "Order placed successfully"