class Solution:

    # recursive case, time limit reached
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        # base case, if n = 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # recursion
        # climb choosing 1 first
        n1 = self.climbStairs(n-1)
        n2 = self.climbStairs(n-2)

        self.memo[n] = n1+n2
        return self.memo[n]