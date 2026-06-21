class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                self.prefix[i] = num
            else:
                self.prefix[i] = self.prefix[i-1] + num

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        if left:
            left_sum = self.prefix[left -  1]
        else:
            left_sum = 0
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)