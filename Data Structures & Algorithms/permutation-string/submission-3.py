class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        if not s1:
            return True

        s1a = [0] * 26
        s2a = [0] * 26
        l = 0
        for r in range(len(s2)):
            s2a[ord(s2[r]) - ord("a")] += 1

            if r - l + 1 > len(s1):
                s2a[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if r == len(s1) - 1:
                for ch in s1:
                    s1a[ord(ch) - ord("a")] += 1
            
            if s1a == s2a:
                return True
        
        return False
            
