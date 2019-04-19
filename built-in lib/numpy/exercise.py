import numpy as np
arr = np.arange(5)
out = np.where(arr % 2 == 1, -1, arr)

print(np.tile(arr, [2]))
print(arr.repeat(2))
print(np.hstack((np.repeat(arr, 2), np.tile(arr, 2))))

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.where(a == b))

a = np.array([2, 6, 1, 9, 10, 3, 27])
print(a[(a>=5) & (a<=10)])

# 对调两列
arr = np.arange(9).reshape((3, 3))
print(arr)
print(arr[:, [2, 0, 1]])

# 翻转行
arr = np.arange(9).reshape((3, 3))
print(arr)
print(arr[::-1])

# 翻转列
arr = np.arange(9).reshape((3, 3))
print(arr)
print(arr[:, ::-1])