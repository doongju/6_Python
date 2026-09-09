colors = ["red","green","blue"]

print(f"colors -> {colors}")

print(f"첫번째 : {colors[0]}")

print(f"마지막 : {colors[-1]}")

print(f"{colors[0:2]}")

mixed = [100,"Hello",True,[1,2,3]]
print(f"mixed : {mixed}")

temp=[]
print(f"mixed --> {bool(mixed)}")
print(f"temp --> {bool(temp)}")


print("="*60)
items = ["에이스","아이비","코피코"]

print(f"items --> {items}")

items.append("오감자")
print(f"append - 맨 뒤에 추가 :{items}")

items.insert(2,"쿠쿠")
print(f"insert - 위치를 지정해서 추가 : {items}")

print("="*60)
items[0] = "ACE"
print(f"특정 인덱스를 지정하여 값을 변경 : {items}")

items.remove("코피코")
print(f" 값을 삭제 : {items}")

snack = items.pop()
print(f"pop - {items} - {snack}")

del items[0]
print(f"del - {items}")

numbers = [5,1,2,7,9,4,1]
print(f"numbers에 7이 있는지 ? {7 in numbers}")
print(f"numbers 에 7이 있는지 ? {numbers.index(7)}")


print(f"{numbers}")
numbers.sort()
print(f"{numbers}")
numbers.sort(reverse=True)
print(f"{numbers}")

fruits = ["banana", "cherry","apple"]
fruits.sort()
print(f"문자열 정렬 -> {fruits}")
fruits.reverse()
print(f"reverse -> {fruits}")

print("="*60)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for value in row:
        print(value,end=" ")
    print()