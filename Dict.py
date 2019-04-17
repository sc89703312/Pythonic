from collections import OrderedDict, _Link, _proxy

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
