nums = [2,2,3,4,5,6,21,2]
count = 0
emp_lst = [] 
for num in nums:
    if count < 2 or emp_lst[count - 2] != num:
        emp_lst.append(num)
        count = count + 1
nums[:] = emp_lst
