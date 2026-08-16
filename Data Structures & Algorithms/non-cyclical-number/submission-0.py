class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def checkHappy(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n_str = str(n)

            new_n = 0
            for num in n_str:
                new_n += int(num) ** 2
            return checkHappy(new_n, seen)
        
        return checkHappy(n, seen)