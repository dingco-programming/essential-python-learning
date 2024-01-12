balance = 0
products = [
    ["콜라", 2000, 5],
    ["사이다", 750, 5],
    ["환타", 1500, 5]
]


# 메뉴 출력
print(f"\n\n자판기 프로그램")
print("-----------------------")
print(f"1. {products[0][0]}({products[0][2]}개) : {products[0][1]} 원")
print(f"2. {products[1][0]}({products[1][2]}개) : {products[1][1]} 원")
print(f"3. {products[2][0]}({products[2][2]}개) : {products[2][1]} 원")
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