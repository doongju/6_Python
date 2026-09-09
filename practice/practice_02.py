# 1. 몸무게(kg)와 키(cm)를 입력받아 BMI 지수를 계산하는 함수를 정의

# we = input("몸무게를 입력하세요(kg) : ")
# he = input("키를 입력하세요(cm) : ")

# we = float(we)
# he = float(he)

# he1 = he / 100
# bmi = we / (he1 * he1)
# bmi = round(bmi, 2)

# print(f"BMI : {bmi}")

# 2. 여러 개의 숫자를 입력받아 평균을 계산하는 함수를 정의
# numbers = []
# print("========== 평균 계산기 ==========")
# while True:
#     value = input("숫자 입력 (q 입력시 종료) : ")
#     if value == "q":
#         break
#     numbers.append(float(value))

# if len(numbers) == 0:
#     print("\n---> 값이 없습니다.")
# else:
#     average = sum(numbers) / len(numbers)
#     print(f"\n---> 평균: {average}")

# 3. 단어 빈도수 분석 함수 정의
message = input("문장을 입력하세요 : ")

unique_char = {ch for ch in message.split()}
print(f"'{message}' 의 고유 문자 : {unique_char}")



 











