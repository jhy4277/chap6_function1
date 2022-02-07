# 함수가 리턴값이 없는 경우에 대한 예제
def printInfo(name, age):
    print("==========")
    print("이름 : ", name)
    print("나이 : ", age)
    print("==========")

    return

end_Input = "y"
print("이름과 나이를 입력해주세요.(입력종료:q)")
while True:
    if end_Input=="n":
        print("입력을 종료")
        break
    elif end_Input=="y":
        name=input("회원명을 입력해주세요: ")
        age=int(input("나이을 입력해주세요: "))
        printInfo(name,age)

    end_Input=input("계속 입력하시겠습니까?(y or n) :")
