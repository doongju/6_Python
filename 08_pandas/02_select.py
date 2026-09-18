from utils.loader import load_csv

df = load_csv()
print(df.head())

print(f"{len(df)} / {df['code'].unique()} 종목")

last_day = df['date'].max()
print(f"마지막 거래일 : {last_day}")

last_history = df[df['date']==last_day].reset_index(drop=True)
print(f"기준일 : {last_day} /{len(last_history)}개 종목")

print(last_history.head())

print(last_history[['code','close','changeRate']].head())

one = last_history['close']
two = last_history[['close']]

print(f"last_histroy['close'] -> {type(one).__name__ } / shape : {one.shape}")
print(f"last_histroy[['close']] -> {type(two).__name__ } / shape : {two.shape}")

print('-'*60)

exps = last_history[last_history['close']>100_000]
print(f"결과 : {len(exps)}건")
print(exps[['code','close']].to_string(index=False))

result = last_history['close']>100_000
print(f"결과 : {result.sum()}건")

# SQL : WHERE 조건1 AND 조건2 / WHERE 조건1 OR 조건2
# Pandas : df[(조건1) & (조건2)] / df[(조건1) | (조건2)]

# 기준데이터: 마지막 거래일 기록
# TODO: 'close'가 50000을 초과하고, 'changeRate'가 0을 초과하는 데이터

both = last_history[(last_history['close']>50_000)&(last_history['changeRate']>0)]
print(f"결과 {len(both)}건")
print(both[['code','close','changeRate']].head(3))

df = last_history
print(" === 가장 비싼 3개 종목 ===")
top = df.sort_values("close",ascending=False).head(3)
print(top[['code','close']])

print(" === 가장 많이 오른 3개 종목 ===")
rise = df.sort_values("changeRate",ascending=False).head(3)
print(rise[['code','close','changeRate']])

print(" === 종가 기준, 1만 ~ 5만 사이의 종목 ===")
result = df[(df['close'] >= 10_000) & (df['close']<50_000)]
print(f" 조회 결과 : {len(result)}")

retsult = df['close'].between(10_000,50_000)
print(f" 조회 결과 : {len(result)}")

print(" === 종목코드가 ~~만 조회 ===")

result = df[df['code'].isin(['G0001','G0050','G0100'])]
print(result)

print('-'*60)

print(" === loc ===")
print(df.loc[0:2])

print(" === iloc ===")
print(df.iloc[0:2])

result = df.loc[df['close']>200_000, ['code','close','volume']].head(3)
print(result)

print('-'*60)

indexed = df.set_index('code')
print(indexed.head(3))

print(indexed.loc['G0001',['close','changeRate']])















