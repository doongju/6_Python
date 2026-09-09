nums=[]
for n in range(1,6):
    nums.append(n)

print(f"nums : {nums}")

nums = [n for n in range(1,6)]
print(f"nums : {nums}")

nums = [n*n for n in range(1,6)]
print(f"nums : {nums}")
print()

nums = [1,2,3,4,5,6]
print(f"짝수만 -- > {[n for n in nums if n%2 ==0]}")
print(f"3의 배수만 -- > {[n for n in nums if n%3 ==0]}")

print("=" *60)

menus = ["제육","햄부기","돈까"]

menus_dict = {m:len(menus) for m in menus}

print(f"menus_dict : {menus_dict}")

menus_dict = {m:len(menus) for m in menus if len(m) == 3}

print(f"menus_dict : {menus_dict}")

message = 'No pain, No gain'

unique_char = {ch for ch in message}
print(f"'{message}' 의 고유 문자 : {unique_char}")

unique_char = {ch for ch in message if ch != ',' or ch != ' '}
print(f"'{message}' 의 고유 문자 : {unique_char}/ ({len(unique_char)})")
