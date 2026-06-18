class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combs = []
        curr_sum = 0

        def dfs(i, target):
            
            # print(curr_sum)
            if target < 0 or i >= len(nums):
                return
            if target == 0:
                result.append(combs.copy())
                return
            
            # include num now and possibly future
            combs.append(nums[i])
            target -= nums[i]
            dfs(i, target)
            # dont include
            combs.pop()
            target += nums[i]
            dfs(i+1, target)
        
        dfs(0, target)
        return result