class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 1

        if not nums:
            return 0

        for n in nums:
            if n - 1 not in nset:
                length = 1
                cur = n
                while cur + 1 in nset:
                    length += 1
                    longest = max(longest, length)
                    cur += 1
        
        return longest