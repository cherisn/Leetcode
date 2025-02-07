class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        return sum(heights[i] != expected[i] for i in range(len(heights)))
"""
        n = 0
        for i in range(len(heights)):
            if(heights[i] != expected[i]):
                n+=1
        return n
"""
