class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combs = []

        def dfs(i):
            curr_sum = sum(combs)
            # print(curr_sum)
            if curr_sum > target or i >= len(nums):
                return
            if curr_sum == target:
                result.append(combs.copy())
                return
            
            # include num now and possibly future
            combs.append(nums[i])
            dfs(i)
            # dont include
            combs.pop()
            dfs(i+1)
        
        dfs(0)
        return result