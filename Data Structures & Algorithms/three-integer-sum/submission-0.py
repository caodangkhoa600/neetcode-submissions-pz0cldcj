class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        n = len(nums)
        i = 0

        while i < n:
            j = i + 1
            k = n - 1

            while j < n and k > 0 and j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = n - 1
                    while j < n and nums[j] == nums[j-1]:
                        j = j + 1

                else:
                    if sum < 0:
                        j = j + 1
                    else:
                        k = k - 1
            i = i + 1            
            while i < n and nums[i] == nums[i-1]:
                i = i + 1 

        return result