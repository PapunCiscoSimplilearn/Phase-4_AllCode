class InventoryService:
    def check_stock(self, product, quantity):
        return product["stock"] >= quantity

    def reduce_stock(self, product, quantity):
        product["stock"] -= quantity
        print("Inventory updated")