from datetime import datetime
from models import GeneralProduct, FreshProduct, OutOfStockError, ProductNotFoundError
from inventory import Inventory
 
def print_menu():
    print("=" * 50)
    print(" 창고 재고 관리 프로그램")
    print("=" * 50)
    print(" 1. 상품 등록")
    print(" 2. 전체 재고 확인")
    print(" 3. 긴급 발주 목록 확인 (재고 10개 미만)")
    print(" 4. 전체 재고 총 금액 확인")
    print(" 5. 입고 처리 (재고 증가)")
    print(" 6. 출고 처리 (재고 감소)")
    print(" 7. 단가 수정")
    print(" 8. 상품 삭제")
    print(" 0. 종료")
    print("=" * 50)
 
def register(inventory):
    print("- 1.일반물품  2.신선식품 -")
    kind = input("등록할 유형 선택: ")
 
    code = input("상품코드: ")
    name = input("품명: ")
    price = int(input("단가: "))
    stock = int(input("재고수량: "))
 
    if kind == "1":
        hazardous = input("위험물 여부(y/n): ").strip().lower() == "y"
        product = GeneralProduct(code, name, price, stock, hazardous)
    elif kind == "2":
        expire_str = input("유통기한(YYYY-MM-DD): ")
        expire_date = datetime.strptime(expire_str, "%Y-%m-%d").date()
        product = FreshProduct(code, name, price, stock, expire_date)
    else:
        print("잘못된 선택입니다.")
        return
 
    inventory.add(product)
    print(f"등록 완료 : {product}")
 
 
def show_all(inventory):
    products = inventory.get_all()
 
    if not products:
        print("등록된 상품이 없습니다.")
        return
 
    for p in products:
        print(p)
 
def show_urgent(inventory):
    urgent_list = inventory.get_urgent_list()
 
    if not urgent_list:
        print("긴급 발주 대상이 없습니다.")
        return
 
    for p in urgent_list:
        print(p)
 
def show_total(inventory):
    print(f"전체 재고 총 금액 : {inventory.get_total_amount():,}원")
 
def do_restock(inventory):
    code = input("상품코드: ")
    amount = int(input("입고수량: "))
 
    try:
        product = inventory.restock(code, amount)
    except ProductNotFoundError as e:
        print(f"입고 실패 : {e}")
    else:
        print(f"입고 완료 : {product}")
 
def do_release(inventory):
    code = input("상품코드: ")
    amount = int(input("출고수량: "))
 
    try:
        product = inventory.release(code, amount)
    except ProductNotFoundError as e:
        print(f"출고 실패 : {e}")
    except OutOfStockError as e:
        print(f"출고 실패 : {e}")
    else:
        print(f"출고 완료 : {product}")
 
def do_update_price(inventory):
    code = input("상품코드: ")
    price = int(input("새 단가: "))
 
    try:
        product = inventory.update_price(code, price)
    except ProductNotFoundError as e:
        print(f"단가 수정 실패 : {e}")
    except ValueError as e:
        print(f"단가 수정 실패 : {e}")
    else:
        print(f"단가 수정 완료 : {product}")
 
def do_remove(inventory):
    code = input("삭제할 상품코드: ")
 
    try:
        product = inventory.remove(code)
    except ProductNotFoundError as e:
        print(f"삭제 실패 : {e}")
    else:
        print(f"삭제 완료 : {product}")
 
def main():
    inventory = Inventory()
 
    while True:
        print_menu()
        choice = input("메뉴 선택 : ")
 
        if choice == "1":
            register(inventory)
        elif choice == "2":
            show_all(inventory)
        elif choice == "3":
            show_urgent(inventory)
        elif choice == "4":
            show_total(inventory)
        elif choice == "5":
            do_restock(inventory)
        elif choice == "6":
            do_release(inventory)
        elif choice == "7":
            do_update_price(inventory)
        elif choice == "8":
            do_remove(inventory)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다.")
 
main()