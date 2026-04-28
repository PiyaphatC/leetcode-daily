a = [1,2,3]
emp = []
for i in a:
    emp.append(str(i))

s = "".join(emp)
print(int(s)+1)