import pandas as pd

df = pd.DataFrame(
    {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss Elizabeth",

        ],

        "Age": [22, 35, 58],

        "Sex": ["male", "male", "female"],

    }
)

print(df)

print(df['Name'])
print(df["Age"])
print(df["Sex"])

print('\n=== 타입 출력 ===')
print(type(df))
print(type(df['Age']))

print('\n=== 이름이 Age인 Series 생성 ===')
ages = pd.Series([22, 35, 44], name='Age')
print(ages)

print('\n=== 기본 통계 함수 ===')
print('max : 최댓값')
print('최대 나이 : ', df['Age'].max())

print('min : 최솟값')
print('최소 나이 : ', df['Age'].min())

print('mean : 평균값')
# print('평균 나이 : ', df['Age'].meam())

print(df.describe())

print('DataFrame의 전체 요약 정보')

print(df.info())

print('\n=== DataFrame에서 특정 행을 선택하는 방법 2가지 ===')

print(df.iloc[1])
print(df.iloc[2])

print(df.loc[0])
print(df.iloc[0])

# print(df.head[0])
# print(df.head[2])

# print(df.tail[0])
# print(df.tail[2])

print('\n=== 열 수정 ===')

# df['Survived'] = [0, 1, 2]



# pf2 = df.copy()
'''
df2.loc[1, 'Age'] = None
print(df2.isnull())

print(df2.dropna(axis=0))

print(df2.fillna(0))

print(df2['Age'].fillna(df['Age'].mean))

# print(df2.fillna(method='ffill'))
print(df2.ffill())

'''
