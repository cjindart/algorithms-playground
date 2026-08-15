class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)

            elif ch == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif ch == "*":
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            elif ch == "/":
                right, left = stack.pop(), stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(ch))
        return stack.pop()