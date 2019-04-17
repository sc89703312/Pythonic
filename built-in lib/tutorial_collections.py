from collections import OrderedDict, defaultdict, deque, Counter, _Link, _proxy
from operator import itemgetter as _itemgetter

# ===========================================================================================
# 1. OrderedDict
# 使用dict时，键值对是无序的，在对dict遍历时，无法确定key的顺序
# 若需要保持key的顺序，可以使用OrderedDict
# OrderedDict本质上是一个环形的双端链表，头和尾用一个 Sentinel 来表示
# 插入键值对时，若键不存在，则需要在 Sentinel.pre位置上插入新节点
# popitem可指明是按照LIFO顺序还是FIFO顺序
keys = ['a', 'b', 'c', 'aaa', 'zzz']
values = [1, 3, 2, 4, 5]

d = dict(zip(keys, values))
print(d)

od = OrderedDict(zip(keys, values))
print(od)

# 可以使用OrderedDict来实现一个定容的FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value, dict_setitem=dict.__setitem__, proxy=_proxy, Link=_Link):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# ===========================================================================================
# 2. Counter
c_empty = Counter()     # a new, empty counter
c_str = Counter("gallahad")     # a new counter from an iterable
c_dict = Counter({'red':4, 'blue': 5})      # a new counter from a mapping
c_keywords_args = Counter(cats=4, dogs=8)   # a new counter from keyword args
print(c_str.items())
print(c_str.most_common())
print(c_dict.values())
print(list(c_keywords_args.elements()))

# update
c_initial = Counter("initial")
print(c_initial.items())
c_initial.update("initialize")
print(c_initial.items())

# soft del and hard del
c_initial['i'] = 0
print(c_initial.items())
del c_initial['i']
print(c_initial.items())

# ===========================================================================================
# 3. defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
# When each key is encountered for the first time, it is not already in the mapping
# d = {}
for k, v in s:
    d[k].append(v)
print(d.items())

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))
