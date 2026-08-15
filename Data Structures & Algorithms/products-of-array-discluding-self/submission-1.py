class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None] * len(nums)
        post = [None] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = postfix
            postfix *= nums[i]
        result = []
        for i in range(len(nums)):
            result.append(pre[i] * post[i])
        return result