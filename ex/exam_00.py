'''
# 1. 1부터 100까지의 정수 중에서 난수를 생성하여 (4, 5) 배열을 만들고 arr에 저장해주세요.
arr = np.random.randint(1, 101, size=(4, 5))
print(arr)
'''
# 2. 생성된 배열의 차원, 형태, 원소 개수를 출력해주세요.
'''
count_nonzero()
- 배열에서 0이 아닌 값의 개수를 세는 함수
- 조건식이 붙는다 True 1, False 0

size
- 배열에 들어 있는 전체 원소의 개수를 반환하는 속성
result[result >= 90].size

arr = np.random.randint(1, 101, size=(4, 5))

print('배열의 차원 :', arr.ndim)
print('배열의 형태 :', arr.shape)
print('배열의 원소개수 :', arr.size)
'''
import numpy as np

np.random.seed(10)

# 3. 첫 번째 행과 세 번째 행만 선택해서 출력해주세요.
arr = np.random.randint(1, 101, size=(4, 5))

# 3. 첫 번째 행과 세 번째 행만 선택해서 출력해주세요.
# 방법 1: 팬시 인덱싱 (원하는 행 번호를 리스트로 전달)
# print(arr[[0, 2]])

# 방법 2: 슬라이싱 (0번부터 끝까지 2칸 간격으로 선택)
# print(arr[0::2])

# 4. 각 행의 평균을 구해주세요.
result = arr.mean(axis=1)
print(result)
# 5. 각 열의 최댓값을 구해주세요.
result = arr.argmax(axis=0)
print(result)

# 6. 50 이상인 값만 추출해주세요.


# 7. 70 이상인 원소가 몇 개인지 출력해주세요.


# 8. 60 이상이면 '합격', 60 미만이면 '불합격'인 새로운 배열을 만들어주세요.


# 9. 전체 배열에서 최댓값의 위치를 (행, 열) 형태로 출력해주세요.


# 10. 배열의 모든 값에 10을 더한 뒤 100을 초과하는 값은 100으로 변경해주세요.