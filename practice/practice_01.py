# 1번째
# name = input("이름 입력 : ")
# se = input("성별(M/F) 입력 : ")
# age = input("나이 입력 : ")
# hei = input("키 입력 : ")
# print(f"이름 : {name} , 성별 : {se} , 나이 : {age}, 키 : {hei}")

# ------------------------------------------------------------------

# 2번째
# lo = input("영문 소문자를 입력하세요 : ")
# print(f"소문자 : {lo}")
# print(f"대문자 : {lo.upper()}")

# ------------------------------------------------------------------

# 3번째
# fir=int(input("첫 번째 정수를 입력하세요 : "))
# se=int(input("두 번째 정수를 입력하세요 : "))
# print(f"합 : {fir+se}")
# print(f"합 : {fir-se}")
# print(f"합 : {fir*se}")
# print(f"합 : {fir//se}")
# print(f"합 : {fir%se}")

# ------------------------------------------------------------------

# 4번째
# fir=int(input("첫 번째 정수를 입력하세요 : "))
# se=int(input("두 번째 정수를 입력하세요 : "))
# print(f"{fir}의 제곱 : {fir **2}")
# print(f"{se}의 제곱 : {int(se**0.5)}")

# ------------------------------------------------------------------

# 5번째
# score = int(input("점수 입력(0~100) : "))
# if score >= 90:
#     grade ="A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# elif 0 < score < 60:
#     grade = "F"
# else:
#     grade = "점수를 올바르게 입력해주세요"
# print(f"{score}점 => {grade}")

# ------------------------------------------------------------------

# 6번째
# for n in range(1,101):
#     if n % 2 == 0:
#         print(n)

# ------------------------------------------------------------------

# 7번째
result = 0
for n in range(1, 101):
    if (n % 3 == 0) and (n % 5 != 0):
        result += n     
print(result)