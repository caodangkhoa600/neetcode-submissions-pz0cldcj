class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        maxLeft = 0
        maxRight = 0
        result = 0

        while start < end:
            maxLeft = max(maxLeft, height[start])
            maxRight = max(maxRight, height[end])

            if maxLeft < maxRight:
                result = result + maxLeft - height[start]
                start = start + 1
            else:
                result = result + maxRight - height[end]
                end = end - 1

        return result