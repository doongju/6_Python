import numpy as np
arr = np.arange(12)
print(arr)
print('-'*60)

arr_2d = arr.reshape(3,4)
print(arr_2d)

print('-'*60)

arr_2d_2 = arr.reshape(2,6)
print(arr_2d_2)

print('-'*60)

arr_2d_3 = arr.reshape(4,-1)
print(arr_2d_3)

print('-'*60)
arr_2d_4 = arr.reshape(-1,6)
print(arr_2d_4)
print('-'*60)

arr_3d = arr.reshape(2,2,3)
print(arr_3d.shape)
arr_3d_1 = arr.reshape(3,2,-1)
print(arr_3d_1)

print('-'*60)

arr_1d = arr_3d.flatten()
print(f"flatten --> {arr_1d}")

arr_1d_2 = arr_3d.ravel()
print(f"ravel --> {arr_1d_2}")

#메모리가 연속적으로 배치된 경우에만 뷰를 반환
#메모리가 불연속적인 경우 (ex. 전치행렬, .T 등) 복사본을 반환
#.base 속성으로 뷰인지 복사본인지 확인 가능!
#ex) arr_1d_2.base is arr_3d=> True (뷰) / False (복사본)

arr_1d_3 = arr_3d.reshape(-1)
print(f"reshape(-1) : {arr_1d_3}")

arr_1d_4 = arr_2d.reshape(-1)
print(f"reshape(-1) : {arr_1d_4}")


