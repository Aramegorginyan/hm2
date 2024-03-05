class Product:
    def __init__(self, product_id, product_name, price, inventory_count):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.inventory_count = inventory_count

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def sell(self, quantity):
        self.inventory_count -= quantity

class DynamicPricing:
    def __init__(self, factor):
        self.factor = factor

    def adjust_price(self, product):
        product.price *= self.factor