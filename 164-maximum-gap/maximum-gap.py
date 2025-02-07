class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0  # No gap if less than 2 elements
        
        # Radix Sort Implementation
        max_value = max(nums)  # Find max value to determine number of digits
        exp = 1  # Exponential divisor (1, 10, 100, ...)

        while max_value // exp > 0:
            radix_array = [[] for _ in range(10)]  # Buckets for digits 0-9
            
            # Distribute elements into buckets based on current digit
            for val in nums:
                radix_index = (val // exp) % 10
                radix_array[radix_index].append(val)

            # Collect elements back into nums
            nums.clear()
            for bucket in radix_array:
                nums.extend(bucket)

            exp *= 10  # Move to the next significant digit

        # Find the maximum gap
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap