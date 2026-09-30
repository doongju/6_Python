import pandas as pd

"""1. pandas를 사용하여 train.csv 파일 데이터를 불러와 DataFrame 으로 저장하시오."""

df = pd.read_csv('rhkwp/data/train.csv')

"""2. 저장된 데이터에서 상위 5개 행을 출력하시오."""
print(df.head())