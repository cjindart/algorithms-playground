class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                cur_len = 1
                while num + 1 in numSet:
                    cur_len += 1
                    num += 1
                longest = max(longest, cur_len)
            
        return longest