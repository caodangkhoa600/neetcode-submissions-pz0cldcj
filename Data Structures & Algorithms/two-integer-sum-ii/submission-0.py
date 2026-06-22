class Solution:
    def search(self, numbers, l, r, target):
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        
        if target - numbers[r] < numbers[l]:
            r = r - 1
        else:
            l = l + 1

        return self.search(numbers, l, r, target)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        return self.search(numbers, l, r, target)