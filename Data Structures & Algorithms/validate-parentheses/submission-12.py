class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for ch in s:
            if ch in m.values():
                stack.append(ch)
            if ch in m.keys():
                if not stack or stack.pop() != m[ch]:
                    return False
        
        return len(stack) == 0
                