'''
# 어노테이션(Annotation): 이 변수나 함수는 이런 타입입니다.라고 설명해주는 표시
# 기본 변수
age = 30

# 어노테이션 추가
# 변수이름: 자료형 = 값
age: int = 30

print(age)

print('\n=== 변수 어노테이션 ===')
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))
print(add('3', '5'))

# 리스트 안에 int가 들어간다는 으미ㅣ
nums = 
'''
