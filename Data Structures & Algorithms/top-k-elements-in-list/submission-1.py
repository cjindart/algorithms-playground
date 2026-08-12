class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        # make freq list
        f = [[] for i in range(len(nums)+1)]

        # add nums to f list at count idx
        for num, count in counts.items():
            f[count].append(num)
        
        # create result array
        result = []
        for i in range(len(f) - 1, 0, -1):
            for num in f[i]:
                result.append(num)
                if len(result) == k:
                    return result