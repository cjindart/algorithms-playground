class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                tmp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = tmp
                j -= 1
            result.append(pairs[:])
        return result