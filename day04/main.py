balance = 0

# 메뉴 출력
print(f"\n\n자판기 프로그램")
print("-----------------------")
print(f"1. 콜라(5개) : 2000 원")
print(f"2. 사이다(5개) : 750 원")
print(f"3. 환타(5개) : 1500 원")
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