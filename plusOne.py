def plusOne(self, digits: List[int]) -> List[int]:
    emp = []
    for i in digits:
        emp.append(str(i))
    ans = str(int("".join(emp))+1)
    ans_lst = [int(c) for c in ans]
    return ans_lst