class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            # non val found, swap it with k (last val found)
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
            # val found
            elif nums[i] == val:
                continue # i increased, k stays
        return k





