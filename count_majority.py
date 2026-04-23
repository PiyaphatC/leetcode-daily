import numpy as np

nums = [3,2,3]

arr = np.array(nums)
values, counts = np.unique(arr, return_counts=True)
most_repeated = values[counts.argmax()]

print(most_repeated.item())