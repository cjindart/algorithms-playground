class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(curSum, 0)
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
        
        return maxSum