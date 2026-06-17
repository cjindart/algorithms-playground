class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0
        r = 0
        while r < len(nums):
            # if val not found, increase both
            if nums[r] != val:
                r += 1
                w += 1
            
            # if val found
            elif nums[r] == val:
                # find next non val until end of list
                while r < len(nums) and nums[r] == val:
                    r += 1
                
                if r == len(nums):
                    # found end of list, jump out of loop
                    break
                # next non val found
                elif nums[r] != val:
                    # replace w with r
                    nums[w] = nums[r]
                    nums[r] = val
                    # update w to next pos, reset r
                    w += 1
                    r = w

                
        return w
                







