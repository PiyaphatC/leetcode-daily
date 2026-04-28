n = 7
ans = 1
count = 0
for i in range(n):
    ans = ans * (n-i)
str_ans = str(ans)
str_ans_lst = [c for c in str_ans]
# print(str_ans_lst)

#counting trailing zero
for i in range(len(str_ans_lst)):
    if str_ans_lst[-i-1] == "0":
        count = count + 1
    else:
        break

print(count)