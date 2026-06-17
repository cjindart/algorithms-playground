class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        def findMax(arr) -> int:
            m = -float("inf")
            for num in arr:
                if num > m:
                    m = num
            return m


        for i, num in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                m = findMax(arr[i+1:])
                arr[i] = m
        return arr


