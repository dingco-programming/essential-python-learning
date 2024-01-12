# 메뉴 출력
print("자판기 프로그램")
print("-----------------------")
print("1. 콜라(5개) : 2000 원")
print("2. 사이다(5개) : 750 원")
print("3. 환타(5개) : 1500 원")
print("-----------------------")
print(f"현재 잔액 : 0 원")
print("-----------------------")
print("")
print("1. 상품 선택")
print("2. 돈 투입")
print("3. 잔액 반환")
print("4. 종료")
print("")

# 메뉴 입력
menu = int(input("메뉴 선택 : "))
print(type(menu))

if menu == 1:
    # 상품 선택
    print("상품 선택")
elif menu == 2:
    # 돈 투입
    print("돈 투입")
elif menu == 3:
    # 잔돈 반환
    print("잔돈 반환")
elif menu == 4:
    print("프로그램 종료")
else:
    print(f">> 1~4까지 숫자를 입력해주세요!")