class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        l = 0
        for num in s:
            if num - 1 not in s:
                v = 1
                j = num
                while j + 1 in s:    
                    j = j + 1
                    v = v + 1
                if v > l:
                    l = v
            
                l = max(l, v)
        return l