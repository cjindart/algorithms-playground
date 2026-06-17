# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1
        self.sort(pairs, s, e)
        return pairs

    def sort(self, arr: List[Pair], s: int, e: int) -> None:
        if (e-s+1) <= 1:
            return
        
        pivot = arr[e]
        left = s

        # partition
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        # move pivot
        arr[e] = arr[left]
        arr[left] = pivot

        # call sort with subarrays
        self.sort(arr, s, left - 1)
        self.sort(arr, left+1, e)