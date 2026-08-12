class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for n in nums:
            # check if start
            if n - 1 not in numSet:
                cur = 1
                while n + cur in numSet:
                    cur += 1
                longest = max(longest, cur)
            
        return longest