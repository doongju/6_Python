import random
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
# message = input("문장을 입력하세요: ")
# words = message.lower().split()
 
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
 
# print("\n[단어 빈도수 결과]")
# for word, count in freq.items():
#     print(f"- {word}: {count}회")
 
# 4. 로또 번호 자동 생성 함수 정의
count = int(input("구매할 로또 게임 수를 입력하세요: "))
 
print("\n[로또 번호 발급 결과]")
for i in range(1, count + 1):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 45))
    numbers = sorted(numbers)
    print(f"{i}게임: {numbers}")
 

# 5. 학생 성적 통계 분석 함수 정의








