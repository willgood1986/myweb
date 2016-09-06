# -*- coding: utf-8 -*-
print('nums=list(range(200)):')
nums = list(range(20))
print(nums)
print("nums[0:2]")
print(nums[0:2])
print("nums[1:2]")
print(nums[1:2])
print("nums[-3:0] length")
print(len(nums[-3:0]))
print("nums[-3:-1] length")
print(len(nums[-3:-1]))
print("When the start index is less than 0, the end index must be None or negative")
print("nums is Iterable[collections]:")
from collections import Iterable
print(isinstance(nums, Iterable))
print("enumerate of nums")
for i, value in enumerate(nums):
     print("index:{index}, value:{val}".format(index=i, val=value))
for x, y in [(1,1), (2, 2), (3, 3)]:
    print("x={x}, y={y}".format(x=x, y=y))
