class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []

        queue = deque() # indices
        l = r = 0

        # [1,2,1,0,4,2,6]
        #  r
        #  l
        # q = [0]
        
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                maxes.append(nums[queue[0]])
                l += 1
            r += 1

        return maxes


            

