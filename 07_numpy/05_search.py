"""     
    넘파이 배열 - 검색, 정렬

    - where : 조건에 맞는 요소의 인덱스 반환 / 값 치환
    - argmax / argmin : 최댓값/최솟값이 있는 인덱스를 반환
    - sort : 정렬
"""
import numpy as np

arr = np.array([10,5,22,15,8,20])
print(arr)

print("== 15보다 큰 값 찾기 ==")
idx_info = np.where(arr>15)
print(f"idx_info : {idx_info}")

arr2 = np.where(arr > 10 , 99 , 0)
print(arr2)

print("="*60)

arr = np.array([[10,20,5],[33,15,40]])

print(f"argmax : {np.argmax(arr)}")
print(f"argmin : {np.argmin(arr)}")

print(arr.flatten())

print(f"열 기준 최댓값 인덱스 : {np.argmax(arr,axis=0)}")
print(f"행 기준 최댓값 인덱스 : {np.argmax(arr,axis=1)}")

print("="*60)
print(f"arr : {arr}")

sorted_arr = np.sort(arr)
print(f"정렬된 배열 : {sorted_arr}")

desc_arr = sorted_arr[::1]
print(desc_arr)


