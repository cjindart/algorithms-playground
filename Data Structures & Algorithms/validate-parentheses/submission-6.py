class Solution:
    def isValid(self, s: str) -> bool:
        # check if empty, return true
        if not s:
            return True

        queue = []
        # add s[0]
        queue.append(s[0])

        for i in range(1, len(s)):
            if s[i] == ')':
                if not queue:
                    return False
                prev = queue.pop()
                if prev != '(':
                    return False

            elif s[i] == '}':
                if not queue:
                    return False
                prev = queue.pop()
                if prev != '{':
                    return False

            elif s[i] == ']':
                if not queue:
                    return False
                prev = queue.pop()
                if prev != '[':
                    return False
            else:
                queue.append(s[i])
        
        if queue:
            return False
        return True
