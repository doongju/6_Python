"""
    출력 함수
    - print() : 화면에 출력
"""
print("="*60)
print("기본 출력 확인")
print("="*60)

print("hello, python")
print('hello, python')


print(100)
print(3.14)
print(10+20)

print("="*60)
print("여러 값을 동시에 출력")
print("="*60)

print("임수진",20,"민트")

print("2026","09","07",sep="-")

print("첫번째 줄",end=" ")
print("두번째 줄")

print("="*60)
print("이스케이프 문자")
print("="*60)

print("이번 줄 다음에 출력하겠습니다. \n 한 줄 개행")
print("탭 간격을 주겠습니다. \t 한 탭 처리")
print("속마음 : \"집 가고 싶다.\"")


print("="*60)
print("문자 형식 지정(문자 포매팅)")
print("="*60)

name = "장재영"
age = 50
height = 122.2

print("이름: %s, 나이: %d, 키: %.1f" % (name, age, height))
print("이름: {}, 나이: {}, 키: {}".format(name, age, height))
print(f"이름: {name}, 나이: {age}, 키: {height}")
print(f"내년{age+1}살이 되면 키는 {height+10}cm가 됩니다.")

print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")

print("="*60)
print("입력 받아보기")
print("="*60)

age_str=input("나이를 입력하세요 : ")

print(f"입력값: {age_str}, 타입: {type(age_str)}")

age = int(age_str)
print(f"입력값: {age}, 타입: {type(age)}")
print(f"내년 나이는 {age+1}살이 됩니다.")








