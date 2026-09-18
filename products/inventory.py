from models import ProductNotFoundError
 
class Inventory:
    def __init__(self):
        self.products = []  # 상품을 담는 리스트 (메모리에만 유지)
 
    def find(self, code):
        for p in self.products:
            if p.code == code:
                return p
 
        raise ProductNotFoundError(code)
 
    def add(self, product):
        self.products.append(product)
        return product
 
    def remove(self, code):
        product = self.find(code)
        self.products.remove(product)
        return product
 
    def restock(self, code, amount):
        product = self.find(code)
        product.restock(amount)
        return product
 
    def release(self, code, amount):
        product = self.find(code)
        product.release(amount)
        return product
 
    def update_price(self, code, price):
        product = self.find(code)
        product.update_price(price)
        return product
 
    def get_all(self):
        return self.products
 
    def get_urgent_list(self):
        return [p for p in self.products if p.is_low_stock()]
 
    def get_total_amount(self):
        return sum(p.get_total_price() for p in self.products)