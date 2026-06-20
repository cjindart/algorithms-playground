class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n, memo):
            
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 2

            if n in memo:
                return memo[n]

            memo[n-1] = climb(n-1, memo)
            memo[n-2] = climb(n-2, memo)

            memo[n] = memo[n-1] + memo[n-2]

            return memo[n]

        num = climb(n, memo)

        return num

