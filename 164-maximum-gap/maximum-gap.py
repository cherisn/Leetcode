class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i]-nums[i-1] for i in range(len(nums)))
