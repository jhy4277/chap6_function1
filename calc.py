# 제곱을 구하는 함수
def square(num):
   #  temp = num * num
    return (num * num)    # 반환값 처리

# 두수 중에서 큰 값을 반환하는 함수
def getmax(x,y):
    # return문은 최소화하는 게 좋은 코드이다.
    temp = 0
    if x>y:
        temp=x
    else:
        temp=y
    return temp


#두 수 중에서 작은 값을 반환하는 함수
def getmin(x,y):
    # return문은 최소화하는 게 좋은 코드이다.
    temp = 0
    if x<y:
        temp=x
    else:
        temp=y
    return temp

# 거듭제곱을  구하여 해당하는 값을 구하는 함수
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result