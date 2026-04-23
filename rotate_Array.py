class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return
        emp_lst = []
        for i in range(len(nums)-k):
            if i == 0:
                for j in range(k):
                    emp_lst.append(nums[j-k])
            emp_lst.append(nums[i])
        nums[:] = emp_lst
        