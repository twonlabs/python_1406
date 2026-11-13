import numpy as np

# 행(세로) axis = 0 / 열
# 열(가로) axis = 1 / 행

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])

# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
print('dtype :', arr.dtype())
print('itemsize :', arr.itemsize())

# 2. axis=0 기준 합을 구하시오.
arr = np.sum(arr, sum())
print('sum :', arr())

# 3. axis=1 기준 평균을 구하시오.
arr = np.average(arr, average())
print('average :', arr())

# 4. arr을 (4,2) 형태로 reshape 하시오.
arr = np.reshape(arr. (4,2))
print('reshape :', arr())

# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
arr = np.reshape(arr. ())

# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?