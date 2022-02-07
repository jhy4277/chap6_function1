# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자.
# 반지름을 사용자로부터 입력을 받음
import math
def sphereVolume(radius):
    volume=(4.0/3.0)*math.pi*math.pow(radius,3)
    return volume

radius=float(input("구의 반지름을 입력하시오 : "))
print("반지름이", radius, "인 구의 부피 : ", round(sphereVolume(radius),2))
