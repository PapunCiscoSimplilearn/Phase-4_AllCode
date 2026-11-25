if __package__:
    from .inventory_service import InventoryService
    from .notification_service import NotificationService
    from .order_repository import MySQLOrderRepository
    from .order_service import OrderService
    from .payment_method import UPIPayment
else:
    from inventory_service import InventoryService
    from notification_service import NotificationService
    from order_repository import MySQLOrderRepository
    from order_service import OrderService
    from payment_method import UPIPayment


product = {
    "name": "Laptop",
    "price": 50000,
    "stock": 10
}

payment = UPIPayment()

inventory = InventoryService()

notification = NotificationService()

repository = MySQLOrderRepository()

order_service = OrderService(
    payment,
    inventory,
    notification,
    repository
)

result = order_service.create_order(
    "Irfan",
    product,
    2
)

print(result)