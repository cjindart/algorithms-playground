class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        queue = deque()
        seen = set()
        longest = 0

        for i in range(len(s)):
            if s[i] not in seen:
                queue.append(s[i])
                seen.add(s[i])
                longest = max(longest, len(queue))

            else:
                while s[i] in seen:
                    char = queue.popleft()
                    seen.remove(char)
                queue.append(s[i])
                seen.add(s[i])
                longest = max(longest, len(queue))
        
        return longest