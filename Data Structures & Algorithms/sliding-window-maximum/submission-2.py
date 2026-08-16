class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []

        queue = deque() # indices
        l = r = 0
        
        while r < len(nums):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if (r + 1) >= k:
                maxes.append(queue[0])
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1
            r += 1

        return maxes