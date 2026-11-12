# 설치가 안될 시
import sys
# 파이썬이 설치된 경로 추출

print(sys.executable)
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름

import numpy as np

print('==== 일반 리스트 =====')
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

print('==== numpy 02 =====')

np.array([1, 2, 3, 4])

arr1 = np.array([1, 2, 3, 4])
arr2 = [1, 2, 3, 4]

print('==== numpy 03 =====')

arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

arr3 = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]],
                [[1, 2, 3, 4], [1, 2, 3, 4]]])

print('2차원 배열 arr2')
print(arr2)

print('3차원 배열 arr3')
print('arr3')

print('==== numpy 04 =====')
a = np.array([1, 2, 3, 4])

print(a + 1)
print(a * 2)
print(a ** 2)

print('==== numpy 05 =====')
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 4]
                [5, 6, 7, 8])
arr3 = np.array([[0.1, 0.2, 0.3, 0.4], [5, 6, 7, 8]],
                [[1, 2, 3, 4], [1, 2, 3, 4]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

print(arr1.size)
print(arr2.size)
print(arr3.size)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

print(arr1.data)
print(arr2.data)
print(arr3.data)

print('==== numpy 06 =====')

arr = np.array([1, 2, 3]
               [4, 5, 6])

