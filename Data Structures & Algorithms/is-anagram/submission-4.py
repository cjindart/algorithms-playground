class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        code1 = [0]*26
        for ch in s:
            n = ord(ch) - ord("a")
            code1[n] += 1
        
        code2 = [0]*26
        for ch in t:
            n = ord(ch) - ord("a")
            code2[n] += 1

        if code1 == code2:
            return True
        return False