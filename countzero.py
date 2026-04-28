n = 7
ans =1 

for i in range(n):
    if i != n:
        ans = ans * (n-i)
str_ans = str(ans)
str_ans_lst = [str(c) for c in str_ans]
count = 0
for i in str_ans_lst:
    if i == "0":
        count += 1


print(count)