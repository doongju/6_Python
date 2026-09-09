point = (10,20)
point2 = 50,60

single = (10,)
single2 = (10)

print(f"point : {point} {type(point)}")
print(f"point2 : {point2} {type(point2)}")

print(f"single : {single}{type(single)}")
print(f"single2: {single2}{type(single2)}")
print()

print(f"point[0] : {point[0]}")
point = (99,20)
print(f"point 자체를 변경 : {point}")
print()

x,y=(2,6)
print(f"x,y : {x}, {y}")

def get_numbers():
    return 77,44

x,y = get_numbers()
print(f"x,y : {x}, {y}")
print()

x, _, z = (10,20,30)
print(f"{x} {z}")

x , *rest = (1,2,3,4,5)
print(f"x : {x} , rest : {rest}")

locations = {
    (35.5451, 126.9750) : "서울역",
    (30.5401, 125.9050) : "부산역"
}


































