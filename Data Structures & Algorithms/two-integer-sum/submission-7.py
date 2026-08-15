class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]
            
            diff = target - num
            diffs[diff] = i
        