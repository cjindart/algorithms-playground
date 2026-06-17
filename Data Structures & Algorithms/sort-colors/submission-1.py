class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for num in nums:
            colors[num] += 1
        
        print(colors)
        
        i = 0
        for n in range(0, len(colors)):
            for _ in range(0, colors[n]):
                nums[i] = n
                i += 1

        return nums
