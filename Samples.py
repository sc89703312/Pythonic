from operator import mul, truth
from functools import reduce

# 1. 置换两个变量的值
a, b = 1, 2
print("a:{}, b:{}".format(a, b))
a, b = b, a
print("a:{}, b:{}".format(a, b))

# 2. 列表求和，最大值，最小值，乘积
numList = [1, 2, 3, 4, 5]

sum = sum(numList)  # sum = 15
maxNum = max(numList)  # maxNum = 5
minNum = min(numList)  # minNum = 1

prod = reduce(mul, numList, 1)  # prod = 120 默认值传1以防空列表报错

# 3. 真值测试
empty_list = []
empty_dict = {}
empty_set = set()
empty_tuple = ()
empty_str = ''

print("empty_list: {}".format(truth(empty_list)))
print("empty_dict: {}".format(truth(empty_dict)))
print("empty_set: {}".format(truth(empty_set)))
print("empty_tuple: {}".format(truth(empty_tuple)))
print("empty_str: {}".format(truth(empty_str)))
print("0: {}".format(truth(0)))
print("None: {}".format(truth(None)))


# 4. 字符串反转
def reverse_str(string):
    return string[::-1]

# 5. 列表连接
strList = ["Python", "is", "good"]
print(" ".join(strList))

# 6. 列表推导式
l = [i**2 for i in range(0, 10) if i % 3 == 0]
print(l)

# 7. 字典默认值
dic = {'name': 'Tim', 'age': 23}
dic['workage'] = dic.get('workage', 0) + 1

# 8. 循环提前跳出
for x in range(0, 5):
    if x == 5:
        print('find 5')
        break
else:
    print('can not find 5!')

# 9. 三元符
a = 3
b = 2 if a > 2 else 1

