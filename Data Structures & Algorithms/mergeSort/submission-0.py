# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1

        # base case
        if (e - s + 1) <= 1:
            return pairs
        
        m = (s+e) // 2
        pairs1 = self.mergeSort(pairs[:m+1])
        pairs2 = self.mergeSort(pairs[m+1:])

        def merge(pairs1: List[Pair], pairs2: List[Pair]) -> List[Pair]:
            res = []
            p1 = 0
            p2 = 0
            while p1 < len(pairs1) and p2 < len(pairs2):
                if pairs1[p1].key <= pairs2[p2].key:
                    res.append(pairs1[p1])
                    p1 += 1
                else:
                    res.append(pairs2[p2])
                    p2 += 1
            while p1 < len(pairs1):
                res.append(pairs1[p1])
                p1 += 1
            while p2 < len(pairs2):
                res.append(pairs2[p2])
                p2 += 1
            return res


        merged = merge(pairs1, pairs2)

        return merged
