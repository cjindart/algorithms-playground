class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)


        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            new_stone = abs(x-y)
            if new_stone != 0:
                heapq.heappush(maxHeap, -new_stone)
        
        if not maxHeap:
            return 0
        return -maxHeap[0]
