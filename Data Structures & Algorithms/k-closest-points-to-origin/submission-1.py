import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(pq, (self.euclid(x, y), point))

        return [heapq.heappop(pq)[1] for _ in range(k)]
    
    
    def euclid(self, x: int, y: int) -> int:
        return (x)**2+(y)**2