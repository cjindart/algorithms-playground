class Solution:
    def isValid(self, s: str) -> bool:
        Map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for ch in s:
            if ch in Map.values():
                stack.append(ch)
        
            else:
                if not stack or stack.pop() != Map[ch]:
                    return False
        
        return len(stack) == 0