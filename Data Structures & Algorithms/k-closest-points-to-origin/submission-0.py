import math
from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = PriorityQueue()
        for point in points:
            x = point[0]
            y = point[1]
            pq.put((self.euclid(x, y), point))

        return [pq.get()[1] for _ in range(k)]
    
    
    def euclid(self, x: int, y: int) -> int:
        return (x)**2+(y)**2