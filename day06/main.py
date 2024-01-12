balance = 0
products = [
    {"name": "콜라", "price": 2000, "count": 5},
    {"name": "사이다", "price": 750, "count": 5},
    {"name": "환타", "price": 1500, "count": 5}
]

# 메뉴 출력
print(f"\n\n자판기 프로그램")
print("-----------------------")
print(f"1. {products[0]['name']}({products[0]['count']}개) : {products[0]['price']} 원")
print(f"2. {products[1]['name']}({products[1]['count']}개) : {products[1]['price']} 원")
print(f"3. {products[2]['name']}({products[2]['count']}개) : {products[2]['price']} 원")
print("-----------------------")
print(f"현재 잔액 : {balance} 원")
print("-----------------------")
print("")
print("1. 상품 선택")
print("2. 돈 투입")
print("3. 잔액 반환")
print("4. 종료")
print("")
try:
    menu = int(input("메뉴 선택 : "))
except:
    print(f">> 숫자로 메뉴를 입력해주세요!")
if menu == 1:
    # 상품 선택
    print("상품 선택")
elif menu == 2:
    # 돈 투입
    money = int(input("투입 금액 입력 (원): "))
    balance = balance + money
    print(f">> {money}원이 투입되었습니다.")
    print(f"현재 잔액 : {balance}")
elif menu == 3:
    # 잔돈 반환
    print(f">> {balance}원을 반환합니다.")
    balance = 0
    print(f"현재 잔액 : {balance}")
elif menu == 4:
    print("프로그램 종료")
else:
    print(f">> 1~4까지 숫자를 입력해주세요!")