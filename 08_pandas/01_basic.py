import pandas as pd
from utils.config import RAW_PATH,ENCODING
datas = [10,20,30,40]

s = pd.Series(datas)
print(s)

print(f"index : {s.index} / {s.index.to_list()}")
print(f"values : {s.values}{type(s.values).__name__}")
print("-"*60)

s = pd.Series(datas,name="sample")
print(s)
print(f"name : {s.name}")
print(f"index : {s.index}")
print(f"values : {s.values}")
print("-"*60)

s = pd.Series(datas,index=['a','b','c','d'])
print(s)
print(f"indxe : {s.index}")
print("-"*60)

s1 = pd.Series([10,20,30],index=['x','y','z'])
s2 = pd.Series([1,2,3],index=['z','y','x'])

print("=====s1=====")
print(s1)
print("=====s2=====")
print(s2)
print()

print(f"s1 + s2 = \n {s1+s2}")

s3 = pd.Series([1,2],index=['x','w'])
print("=====s3=====")
print(s3)
print()

print(f"s1 + s3 = \n {s1+s3}")
print("+"*60)

data = {
    "이름" : ["하루견과","뼈건강비타민","페레로로쉐"],
    "가격" : [2000,4000,3500],
    "재고" : [10,5,20]
}

df = pd.DataFrame(data)
print(df)

print(f"dtypes : \n{df.dtypes}") # 각 열의 데이터 타입
print(f"shape : {df.shape}") # 행, 열의 개수
print(f"index : {df.index}") # 행 인덱스
print(f"colums : {df.columns}") # 열 이름(컬럼명)

print("+"*60)

df = pd.read_csv(RAW_PATH,encoding=ENCODING)
print(df.head())
print(f"close dtype : {df['close'].dtypes}")
print(f"data dtype : {df['date'].dtypes}")

print("+"*60)

df = pd.read_csv(RAW_PATH,
                 encoding=ENCODING,
                 parse_dates=["date"], # date 열은 datetime으로 처리
                 na_values=["N/A", "-"], # 결측으로 취급할 문자들
                 thousands=","   # '1,000,000' 이런식으로 저장된 데이터를 숫자로 처리
                 )
print(df.head())
print(f"close dtype : {df['close'].dtypes}")
print(f"data dtype : {df['date'].dtypes}")

print(f"date unique : {df['date'].unique()}")

# date 열에는 2026-09-17, 20260917, 2026.09.17 형태들로 섞여있음!
#parse_dates 옵션은 해당 열 전체가 같은 형식일 경우에만 적용됨 .

df['date'] = pd.to_datetime(df['date'], format='mixed')
print(f"to_datetime -> {df['date'].dtypes}")

print(df.head(3)) # 숫자 만큼 조회
print(df.shape)
df.info() # 불러온 데이터의 컬럼별 데이터 개수, 타입 등을 확인
print(df.dtypes)















