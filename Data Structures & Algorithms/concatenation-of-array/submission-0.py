class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create the new list
        n = len(nums)
        ans = [0] * 2 * n

        # loop through current list, append to i, and i + len
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+n] = num

        return ans