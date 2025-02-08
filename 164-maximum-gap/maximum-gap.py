class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        
        max_val=max(nums)
        exp=1

        while max_val//exp>0:
            radix_array=[[]for _ in range(10)]
            for val in nums:
                radix_index=(val//exp)%10
                radix_array[radix_index].append(val)
            nums.clear()
            for buckets in radix_array:
                nums.extend(buckets)
            exp*=10
        mdiff=0
        for i in range(1,len(nums)):
            mdiff=max(mdiff,nums[i]-nums[i-1])
        return mdiff

