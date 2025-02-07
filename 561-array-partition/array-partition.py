#USED DEFAULT SORT IN PYTHON IF I NEED TO SORT IN DESC I NEED TO USE 
#nums.sort(reverse=True)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        add = 0
        i=0
        while i < len(nums):  # Extra condition check every loop
            add += nums[i]
            i += 2  # Manually incrementing i 
        return add
"""
        for i in range(0,len(nums),2):
            add+=nums[i]
        return add  
"""