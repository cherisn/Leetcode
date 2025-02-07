"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
"""
class Solution:
    def arrayPairSum(self, nums: List[int]):
        def partition(nums,low,high):
            pivot=nums[high]
            i=low-1
            for j in range (low,high):
                if nums[j]<=pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
            nums[i+1],nums[high]=nums[high],nums[i+1]
            return i+1

        def quicksort(nums,low=0,high=None):
            if high is None:
                high=len(nums)-1
            if low<high:
                pivot_index=partition(nums,low,high)
                quicksort(nums,low,pivot_index-1)
                quicksort(nums,pivot_index+1,high)
        quicksort(nums)

        n=0
        for k in range(0,len(nums),2):
            n+=nums[k]
        return n

        
