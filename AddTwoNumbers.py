l1 = [1,2,3]
l2 = [3,4]

sum = 321 + 43
print(sum)
l1_reverse = list(reversed(l1))
l2_reverse = list(reversed(l2))

value1 =  "".join(str(d) for d in l1_reverse)
value2 =  "".join(str(d) for d in l2_reverse)
print(int(value1)+ int(value2))
