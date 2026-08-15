class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sa = [0] * 26
        ta = [0] * 26
        for i in range(len(s)):
            sa[ord(s[i]) - ord("a")] += 1
            ta[ord(t[i]) - ord("a")] += 1
        
        return sa == ta