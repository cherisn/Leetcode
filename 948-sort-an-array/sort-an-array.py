#USED MERGE SORT
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            lefthalf=nums[:mid]
            righthalf=nums[mid:]
            sortedleft=mergesort(lefthalf)
            sortedright=mergesort(righthalf)

            return merge(sortedleft,sortedright)

        def merge(left,right):
            result=[]
            i=j=0
            while i < len(left) and j < len(right):
                if left[i]<right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i::])
            result.extend(right[j::])
            return result
        return mergesort(nums)
