import numpy as np
nums = [0,1,2,3,6,7,8,11,5,4,0,1]
nums_arr   = np.array(nums)
sorted_arr = np.sort(nums_arr)
unique     = np.unique(sorted_arr)
best    = 0 if len(unique) == 0 else 1
current = 1
print(unique)
for i in range(1, len(unique)):
    if unique[i-1] + 1 == unique[i]:
        current += 1
        best = max(best, current)
    else:
        current = 1

print(best)