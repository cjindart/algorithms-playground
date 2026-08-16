class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0

        for i, ch in enumerate(s):
            count[ch] = 1 + count.get(ch, 0)
            while (i - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, i - l + 1)

        return longest