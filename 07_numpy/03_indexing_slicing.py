import numpy as np
from load_util import load_one_stock

arr = np.array([10,20,30,40,50])
print(f"arr : {arr}")

print(f"첫 번쨰 위치 : {arr[0]}")
print(f"마지막 위치 : {arr[-1]}")

print(f"1~2 위치 : {arr[1:3]}")
print(f"0~2 위치 : {arr[:3]}")
print(f"3~끝 위치 : {arr[3:]}")

print(f"2칸 건너뛰면서 슬라이싱 : {arr[::2]}")
print(f"역순으로 슬라이싱 : {arr[::-1]}")

print("="*60)
data_list = [1,2,3,4]
part_list = data_list[1:3]
part_list[0]=999

print(f"원본 : {data_list} \n슬라이싱 : {part_list}")
print('-'*60)
arr = np.array(data_list)
view = arr[1:3]
view[0]=999

print(f"원본 배열 : {arr}\n슬라이싱 : {view}")
print('-'*60)
arr = np.arange(10)
view=arr[2:5]
copy = arr[2:5].copy()
copy[0]=999
print(f"원본 : {arr} \n 복사 : {copy}")

print(f"view --> {view.base is arr}")
print(f"copy --> {copy.base is arr}")

rsh = arr.reshape(2,5)
print(f"reshape --> {rsh.base is arr}")

rv = arr.ravel()
print(f"ravel --> {rv.base is arr}")

ft = arr.flatten()
print(f"flatten --> {ft.base is arr}")

print("="*60)
def normalize_wrong(arr):
    last_5 = arr[-5:]
    last_5 -= last_5.min()
    return last_5

prices = load_one_stock(0)[:10].copy()
print(f"prices : {prices}")

backup = prices.copy()

result = normalize_wrong(prices)
print(f"== normalize_wrong ==")
print(f"원본 : {prices}")
print(f"결과 : {result}")

result = normalize_wrong(backup)
print(f"== normalize_wrong ==")
print(f"원본 : {backup}")
print(f"결과 : {result}")







