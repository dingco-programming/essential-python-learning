import time
from machines.vending_machine import VendingMachine

vm = VendingMachine([
    {"name": "콜라", "price": 2000, "count": 5},
    {"name": "사이다", "price": 750, "count": 5},
    {"name": "환타", "price": 1500, "count": 5}
])

while True:
    menu = vm.input_menu()
    if menu == 1:
        vm.select_product()
    elif menu == 2:
        vm.insert_money()
    elif menu == 3:
        vm.return_balance()
    elif menu == 4:
        print("프로그램 종료")
        break
    else:
        print(f"잘못된 메뉴 : {menu}")
    time.sleep(2)