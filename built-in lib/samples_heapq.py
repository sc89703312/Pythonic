from heapq import *
# ===========================================================================================
# 可加入tuple 按位进行比较
h = []
heappush(h, (1, 'abcd'))
heappush(h, (1, 'abcc'))
print(heappop(h))

# ===========================================================================================
# 打印
# 默认是一个小顶堆
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# ===========================================================================================
h = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(nsmallest(2, h))
print(nlargest(2, h))