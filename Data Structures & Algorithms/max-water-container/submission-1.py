class Solution:
    def cal(self, height, i, j):
        return (j - i) * height
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        result = 0
        while l < r:
            t = self.cal(min(height[l], height[r]), l, r)
            if t > result:
                result = t
            
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        
        return result
        