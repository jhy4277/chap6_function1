# 섭씨온도를 사용자로부터 입력을 받고 화씨온도로 변환하여 반환하는 함수 ftoc()를 작성하시오.

# 함수선언 및 구현
def ftoc(temp_f):
    temp_c = (5.0*(temp_f-32.0))/9.0
    return temp_c

temp_f= float(input("화씨온도를 입력해주세요 : "))
# 함수 호출
print("화씨온도인 ", temp_f,"를 섭씨온도로 변환한 값 : ", round(ftoc(temp_f),2))