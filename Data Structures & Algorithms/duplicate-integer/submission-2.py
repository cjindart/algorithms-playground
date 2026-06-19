class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                print(num)
                return True
        
        return False