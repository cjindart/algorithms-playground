class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # store anagrams together
        hist = {}
        for s in strs:
            # see how many of each letter, and use this as key in hist
            code = [0] * 26
            for ch in s:
                # get num for ch, i.e. a->0
                n = ord(ch) - ord("a")
                code[n] += 1
            
            key = tuple(code)
            if key in hist:
                hist[key].append(s)
            else:
                hist[key] = [s]
        
        # create return list
        result = []
        for key, values in hist.items():
            result.append(values)
        
        return result