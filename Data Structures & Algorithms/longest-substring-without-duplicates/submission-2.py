class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        longest = 0
        seen = set()

        cur = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                cur -= 1
                l += 1
            
            seen.add(s[r])
            cur += 1
            longest = max(longest, cur)
            r += 1

        return longest