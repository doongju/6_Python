import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

"""1. pandas를 사용하여 train.csv 파일 데이터를 불러와 DataFrame 으로 저장하시오."""

df = pd.read_csv('rhkwp/data/train.csv')

"""2. 저장된 데이터에서 상위 5개 행을 출력하시오."""
print(df.head())
print('-' * 60)
"""
    3. 각 열의 이름, 결측치 여부, 데이터 타입(dtype)을 한 번에 확인하시오.
    `df.info()`를 실행한 후, 출력 결과를 바탕으로 다음을 기술하시오.

    - 결측치가 존재하는 열과 결측 개수
    - `dtype`이 예상과 다르거나 주의가 필요한 열
"""
df.info()
null_count = df.isnull().sum()
print(null_count)
print('-' * 60)

# 4. Age(나이), Fare(요금) 열의 평균값, 최솟값, 최댓값을 구하시오. (실수형 결과 소수점 둘째 자리 반올림)
result = df[['Age', 'Fare']].agg(['mean', 'min', 'max'])
print(result.round(2))
print('-' * 60)

# ### 5. 탑승객 중 생존자와 사망자가 각각 몇 명인지 계산하시오.
# - 생존자 : `Survived`=1 / 사망자 : `Survived`=0

survived_counts = df['Survived'].value_counts()
print(survived_counts)

print('=' * 60)

# 6. 객실 등급(Pclass)별로 탑승객이 몇 명인지 계산하시오.
pclass_counts = df['Pclass'].value_counts()
print(pclass_counts)

print('=' * 60)
# 7. 나이가 50세 이상인 탑승객만 추출하여 새로운 데이터프레임을 만드시오.

passenger = df[df['Age'] >= 50]
print(passenger)

print('=' * 60)

# 8. 탑승객을 나이대 기준으로 그룹화하여 새로운 열 AgeGroup을 추가한 후, 상위 5개 행을 확인하시오.
conditions = [
    (df['Age'] >= 0) & (df['Age'] < 10),
    (df['Age'] >= 10) & (df['Age'] < 20),
    (df['Age'] >= 20) & (df['Age'] < 30),
    (df['Age'] >= 30) & (df['Age'] < 40),
    (df['Age'] >= 40) & (df['Age'] < 50),
    (df['Age'] >= 50) & (df['Age'] < 60),
    (df['Age'] >= 60),
]
choices = ['아동', '10대', '20대', '30대', '40대', '50대', '60대 이상']

df['AgeGroup'] = np.select(conditions, choices, default='미확인')
print(df[['Age', 'AgeGroup']].head())
print('=' * 60)

# 9. 성별(Sex)과 객실 등급(Pclass)을 기준으로 그룹화하여 각각의 평균 생존율을 계산하시오 (소수점 둘째 자리 반올림)
survival_rate = df.groupby(['Sex', 'Pclass'])['Survived'].mean()
print(survival_rate.round(2))
print('=' * 60)

"""
    10. 나이대별 평균 생존율을 계산하시오.

    - 8번에서 생성한 `AgeGroup` 열을 기준으로 그룹화하여 계산하시오. (소수점 둘째 자리 반올림)
"""
AG = df.groupby(['AgeGroup'])['Survived'].mean()
print(AG.round(2))
print('=' * 60)

# 11. 각 열에 존재하는 결측치(NaN)의 총 개수와 전체 데이터 대비 비율을 계산하여 내림차순으로 출력하시오. (비율 소수점 둘째 자리 반올림)
null_count = df.isnull().sum()
null_rate = df.isnull().mean() * 100
missing_df = pd.DataFrame(
    {'결측치 개수': null_count, '비율(%)': null_rate.round(2)}
)
missing_df = missing_df.sort_values(by='결측치 개수', ascending=False)
print(missing_df)
print('=' * 60)

"""
    12. `Sex`열의 'male'은 0으로, 'female'은 1로 변경하여 Gender_Encoded라는 새로운 열을 추가하시오.
    - `map()`, `replace()`, `apply()` 중 편한 방식을 사용해도 됩니다.
"""
df['Gender_Encoded'] = df['Sex'].map({'male': 0, 'female': 1})

print(df[['Sex', 'Gender_Encoded']].head())
print('=' * 60)

# 13. 탑승지(Embarked)별로 승객이 지불한 요금(Fare)의 평균을 계산하시오. (소수점 둘째 자리 반올림)
vudrbs = df.groupby(['Embarked'])['Fare'].mean()
print(vudrbs.round(2))
print('=' * 60)

# 14. Pclass를 인덱스로, Sex를 컬럼으로, 값으로 Fare의 평균을 사용하여 피벗 테이블을 생성하시오. (소수점 둘째 자리 반올림)
pivot = df.pivot_table(
    index='Pclass', columns='Sex', values='Fare', aggfunc='mean'
)
print(pivot.round(2))
print('=' * 60)

# 15. SibSp (형제/배우자 수)와 Parch (부모/자녀 수)를 합산하여
#      FamilySize 열을 추가하고, 이 열의 요약 통계를 확인하세요. (소수점 둘째 자리 반올림)
df['FamilySize'] = df['SibSp'] + df['Parch']
print(df['FamilySize'].describe().round(2))
print('=' * 60)

"""
16. Name 열에서 호칭(Mr., Mrs., Miss., Master. 등)을 정규 표현식 또는 문자열 함수를 사용하여 추출하고 Title이라는 새로운 열을 생성한 뒤, 가장 흔한 5개의 호칭을 출력하시오.
"""
df['Title'] = df['Name'].str.extract(r', ([A-Za-z]+)\.', expand=False)
print(df['Title'].value_counts().head(5))
print('=' * 60)

"""
17. 16번에서 생성한 Title 열을 기준으로 그룹화하여, 각 호칭별 승객 수, 평균 나이, 평균 생존율을 한 번에 계산하시오. (소수점 둘째 자리 반올림)
"""
title_stats = df.groupby('Title').agg(
    승객수=('PassengerId', 'count'),
    평균나이=('Age', 'mean'),
    평균생존율=('Survived', 'mean'),
)
print(title_stats.round(2))
print('=' * 60)

# 18. 생존한 사람과 사망한 사람의 나이(Age) 분포를 비교할 수 있도록 시각화하시오.
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6))

for value, name in [(1, '생존'), (0, '사망')]:
  ages = df.loc[df['Survived'] == value, 'Age'].dropna()
  sns.kdeplot(ages, ax=ax, label=name, fill=True)

ax.set_title('생존 여부에 따른 나이 분포')
ax.set_xlabel('나이 (Age)')
ax.set_ylabel('밀도 (Density)')
ax.legend(title='생존 여부')
fig.savefig('age_distribution.png', dpi=150, bbox_inches='tight')
plt.close(fig)

print('=' * 60)

# 19. 16번에서 추출한 Title과 Pclass를 동시에 고려하여 해당 그룹의 나이 중앙값으로 Age 열의 결측치를 대치하시오. (원본 프레임에 적용)
group_median = df.groupby(['Title', 'Pclass'])['Age'].transform('median')
df['Age'] = df['Age'].fillna(group_median)
print(df['Age'].isna().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
print('=' * 60)

# 20. Survived, Pclass, Age, SibSp, Parch, Fare 등의 수치형 변수들 간의 상관관계 행렬을 계산하고, 소수점 둘째 자리까지 반올림하여 출력한 뒤 히트맵(Heatmap) 으로 시각화하시오.
num_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

corr = df[num_cols].corr()

# 상관관계 값 소수점 둘째 자리까지 반올림하여 출력
print(corr.round(2))
print('=' * 60)

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
ax.set_title('수치형 변수 상관관계 히트맵')

fig.savefig('correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close(fig)