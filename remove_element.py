import numpy as np

nums = [1,2,3,4,5,4]
val = 2
lst = []
k = 0
for num in nums:
    if num == val:
        num == np.nan
        lst.append(np.nan)
    else:
        lst.append(num)
        k = k + 1

print(lst)
print(k)