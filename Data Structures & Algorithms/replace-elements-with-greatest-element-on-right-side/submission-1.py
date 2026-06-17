class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [None] * len(arr)
        
        m = -float("inf")
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                m = arr[i]
                result[i] = -1
            else:
                result[i] = m
                if arr[i] > m:
                    m = arr[i]
        return result
