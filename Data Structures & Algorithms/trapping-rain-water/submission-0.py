class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        m = 0
        for i in range(len(height)):
            maxLeft[i] = m
            m = max(m, height[i])
        m = 0
        for i in range(len(height) - 1, -1, -1):
            maxLeft[i] = min(maxLeft[i], m)
            m = max(m, height[i])

        for i, water in enumerate(maxLeft):
            maxLeft[i] = max(0, maxLeft[i] - height[i])

        return sum(maxLeft)