class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        for i, num in enumerate(nums2):
            map2[num] = i
        
        res = []
        for num in nums1:
            res.append(map2[num])
        
        return res
        