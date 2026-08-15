class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through, create key of ch counts, add to dict list
        hist = {}

        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord("a")] += 1
            key = tuple(key)

            if key in hist:
                hist[key].append(s)
            else:
                hist[key] = [s]
        
        result = []
        for key, value in hist.items():
            result.append(value)
        
        return result
