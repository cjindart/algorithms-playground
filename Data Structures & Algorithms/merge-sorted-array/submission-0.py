class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[end] = nums1[m]
                end -= 1
                m -= 1
            else:
                nums1[end] = nums2[n]
                end -= 1
                n -= 1

        if n >= 0:
            while end >= 0 and n >= 0:
                nums1[end] = nums2[n]
                end -= 1
                n -= 1
        else:
            while end >= 0 and m >= 0:
                nums1[end] = nums1[m]
                end -= 1
                m -= 1
        return nums1