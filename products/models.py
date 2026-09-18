from datetime import date

class OutOfStockError(Exception):
    """ 출고 수량이 현재 재고보다 많을 때 발생하는 예외 """
    def __init__(self, code, name, stock, amount):
        self.code = code
        self.name = name
        self.stock = stock 
        self.amount = amount
        super().__init__(
            f"[{code}] {name} 재고 부족: 현재 {stock}개, 요청 {amount}개"
        )
 
class ProductNotFoundError(Exception):
    """ 상품 코드로 상품을 찾지 못했을 때 발생하는 예외 """
    def __init__(self, code):
        self.code = code
        super().__init__(f"상품 코드 '{code}'를 찾을 수 없습니다.")
 
class Product:
    LOW_STOCK = 10 

    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
 
    def get_price(self):
        return self.price
 
    def get_total_price(self):
        return self.get_price() * self.stock
 
    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("단가는 0 이상이어야 합니다.")
        self.price = new_price
 
    def restock(self, amount):
        self.stock += amount
        return self.stock
 
    def release(self, amount):
        if amount > self.stock:
            raise OutOfStockError(self.code, self.name, self.stock, amount)
 
        self.stock -= amount
        return amount
 
    def is_low_stock(self):
        return self.stock < Product.LOW_STOCK
 
    def __str__(self):
        return (
            f"[{self.code}] {self.name} | 단가: {self.get_price():,}원 "
            f"| 재고: {self.stock}개"
        )
 
class GeneralProduct(Product):
    def __init__(self, code, name, price, stock, is_hazardous=False):
        super().__init__(code, name, price, stock) 
        self.is_hazardous = is_hazardous
 
    def __str__(self):
        hazard = "위험물 O" if self.is_hazardous else "위험물 X"
        return f"{super().__str__()} | 일반물품 ({hazard})"
 
class FreshProduct(Product):
    DISCOUNT_DAYS = 3  
    DISCOUNT_RATE = 0.5  
    def __init__(self, code, name, price, stock, expire_date):
        super().__init__(code, name, price, stock)
        self.expire_date = expire_date
 
    def days_left(self):
        return (self.expire_date - date.today()).days
 
    def get_price(self):
        if self.days_left() <= FreshProduct.DISCOUNT_DAYS:
            return int(self.price * (1 - FreshProduct.DISCOUNT_RATE))
        return self.price
 
    def __str__(self):
        d = self.days_left()
        status = f"D-{d}" if d >= 0 else f"기한초과({-d}일 경과)"
        discount = " [할인 적용중]" if self.get_price() != self.price else ""
        return (
            f"{super().__str__()} | 신선식품 | 유통기한: "
            f"{self.expire_date.isoformat()} ({status}){discount}"
        )