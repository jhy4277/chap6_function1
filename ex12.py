# 사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는 decTobin(num)을 작성하기

def decTobin(num):
    binary = ""

    while num!=0:
        value=num%2
        if value==0:
            binary ="0" + binary
        else:
            binary ="1" + binary
        num = num//2
        print("num : ", num)
    return binary

decNum= int(input("10진수를 입력하세요 : "))
print("10진수 ", decNum, "을 2진수로 변경한 값 : ", decTobin(decNum))

# 파이썬에서 제공하는 진법 변환 함수들
# print(bin(10))을 하면 0b1010이 나오고,  print(int("0b1010",2))를 하면 10이 나옴