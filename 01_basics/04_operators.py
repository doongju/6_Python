"""
    연산자
"""

print("=" * 60)
print("산술 연산자")
print("=" * 60)

print(f"7 + 3 = {7 + 3}")
print(f"7 - 3 = {7 - 3}")
print(f"7 x 3 = {7 * 3}")
print(f"7 / 3 = {7 / 3}")   # 실수 나눗셈
print(f"7 / 3 = {7 // 3}")  # 정수 나눗셈
print(f"7 % 3 = {7 % 3}")   # 나머지 연산
print(f"7 ** 3 = {7 ** 3}") # 거듭제곱 연산. 7을 3번 곱함
print()

print(f"실수 나눗셈 타입 : {type(7 / 3)}")
print(f"실수 나눗셈 타입 : {type(6 / 3)}") # 타입은 항상 float

print(f"-7 / 3 = {-7 / 3}")
print(f"-7 // 3 = {-7 // 3}")  # 자바에서는 버림처리, 파이썬에서는 내림처리

print("=" * 60)
print("비교, 논리 연산자")
print("=" * 60)

a, b = 2, 5
print(f"a, b --> {a} {b}")
print(f"a == b --> {a == b}")
print(f"a != b --> {a != b}")
print(f"a < b --> {a < b}")
print(f"a >= b --> {a >= b}")
print()

# 논리 연산자 : 자바에서 &&, ||, ! 연산자 아닌
#               파이썬에서는 and, or, not 사용
print(f"and --> {True and True}")
print(f"or --> {True or False}")
print(f"not --> {not False}")

# a 값이 -5 ~ 5 사이의 값인가?
print(f"-5 <= a <= 5 결과: {-5 <= a and a <= 5}")

print(f"{-5 <= a <= 5}")        # 연쇄 비교 가능!

print("=" * 60) # 2026/09/08
print("멤버쉽 연산자(in) 식별 연산자(is)")
print("=" * 60)

members=["홍길동", "김철수", "박영희"]
print(f" -> {members}")
print(f"홍길동 in members --> {'홍길동' in members}")
print(f"이순신 in members --> {'이순신' in members}")

print(f"'이순신' 포함하지않는가 -> {'이순신' not in members}")
print(f"{'ll' in 'hello'}")

print()

x =[1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x : {x} / y : {y} / z : {z}")

print(f"배열 값 비교 : {x == y}")  # 값 비교
print(f"객체 주소 비교 : {x is y}")  # 객체 주소 비교
print(f"객체 주소 비교 : {x is z}")  # 객체 주소 비교

data = None
print(f"data is None --> {data is None}")
print(f"data is not None --> {data is not None}")
print()

print("=" * 60)
print("복합 대입 연산자")
print("=" * 60)

x=10
print(f"x : {x}")

x += 5
print(f"x += 5 --> {x}")

x -= 3
print(f"x -= 3 --> {x}")

x *= 2
print(f"x *= 2 --> {x}")

x /= 4
print(f"x /= 4 --> {x}")
