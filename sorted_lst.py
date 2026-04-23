import numpy as np

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

emp_lst = []
for i in range(m):
    emp_lst.append(nums1[i])
for j in range(n):
    emp_lst.append(nums2[j])

arr = np.array(emp_lst)
sorted_arr = np.sort(arr)
arr_to_lst = sorted_arr.tolist()

nums1[:] = arr_to_lst

print(nums1)