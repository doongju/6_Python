print("=" * 60)
print("for문 --> 항상 for-each")
print("=" * 60)

members = ["장재영", "오범영", "김종혁"]

for m in members:
    print(f"{m}님, 환영합니다")

print()
for c in "Happy":
    print(c, end = " ")

print("=" * 60)
print("range 내장 함수 사용")
print("=" * 60)

print(f"range(5) -> {list(range(5))}")
print(f"range(1,6) -> {list(range(1,6))}")
print(f"range(0,10,2) -> {list(range(0, 10, 2))}")
print(f"range(-5,0,1) -> {list(range(-5,0,1))}")

for i in range(5):
    print(f"i : {i}")
print()

for i in range(len(members)):
    print(f"[{i}] : {members[i]}")

print("=" * 60)
print("enumerate() - 번호와 값을 함께")
print("=" * 60)

for i, m in enumerate(members):
    print(f"[{i}] : {m}")
print()

for i, m in enumerate(members,start=1):
    print(f"[{i}] : {m}")

print("=" * 60)
print("zip() - 여러 리스트를 동시에")
print("=" * 60)

names = ["샘숭", "로우닉스", "코코아"]
today = [275000, 1845000 ,35850]
yesterday = [175000, 2045000, 25850]

for name,now,prev in zip(names , today , yesterday):
    diff = now - prev
    print(f"{name:<10} : {now:<8}원 {diff}")

print("=" * 60)
print("while")
print("=" * 60)

count = 0
while count < 5:
    print(f"count : {count}")
    count += 1
print()

n = 1

while True:
    if n> 3:
        break
    print(f"n : {n}")
    n += 1

print("=" * 60)
print("break / continue / for-else")
print("=" * 60)

print("1~10 범위에서 홀수만 출력, 단 7을 넘으면 중단")
for n in range(1,11):
    if n % 2 == 0:
        continue
    if n > 7:
        break
    print(n,end=" ")
print()

print(f"{members}")

for m in members:
    if m == "장재영":
        print("찾")
        break
else:
    print("찾 없")

print()

for m in members:
    if m == "재영":
        print("찾")
        break
else:
    print("찾 없")






















