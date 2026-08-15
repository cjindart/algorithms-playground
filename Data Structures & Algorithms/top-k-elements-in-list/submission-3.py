class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        f = [[] for i in range(len(nums) + 1)]

        for key, count in counts.items():
            f[count].append(key)
        
        result = []
        for i in range(len(f) - 1, -1, -1):
            for n in f[i]:
                result.append(n)
            if len(result) == k:
                return result