# 간단한 사칙연산 계산기 만들기
# 더하기 함수
def add(x,y):
    return x+y

# 빼기 함수
def substract(x,y):
    return x-y

# 곱하기 함수
def multiply(x,y):
    return x*y

# 나누기 함수
def devide(x,y):
    return round((x/y),2)

n1=float(input("첫번째수 입력: "))
n2=float(input("두번째수 입력: "))
op=input("원하는 연산을 입력(+, -, *, /) :")

#연산자에 의해서 분기를 시킨다.

temp = "y"
while True:
    if temp == "n":
     break

    else:
        if op == "+":
            print(add(n1,n2))
        elif op == "-":
            print(substract(n1, n2))

        elif op == "*":
            print(multiply(n1, n2))

        elif op == "/":
            print(devide(n1, n2))
        else:
            print("잘못된 연산자 입니다.")

    temp = input("계산을 계속 하시겠습니까?(y,n)")