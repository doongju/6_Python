import numpy as np
from load_util import load_matrix,load_column
arr = np.array([10,25,30,15,40])
mask=arr>20

print(f"arr:{arr}")
print(f"arr>20 : {mask}")

print(f"arr[mask] : {arr[mask]}")
print(f"mask.sum() : {mask.sum()}")

matrix = load_matrix()
big = matrix >500_000
print(f"matrix > 500_000 :: shape {big.shape}, dtype {big.dtype}")
print(f"True의 개수 : {big.sum()}개 / 전체 : {matrix.size}개")

print(f"{matrix[big].shape}")

print('-'*60)

result = np.diff(matrix,axis=1)/matrix[:,:-1]
print(result)

cond1 = result > 0.03

volumes = load_column("volume")[:,1:]
cond2 = volumes > 2_000_000

both = cond1 & cond2
print(f" 수익률이 3% 이상이고, 거래량이 200만주 이상 : {both.sum()}")
print(f" 수익률이 3%가 되지않는 건수 : {(~cond1).sum()}")

sample = np.array([0.05,-0.02,0.0,0.12,-0.15])
sample2 = np.where(sample > 0, "up",
         np.where(sample < 0,"down","keep"))

print(sample2)
