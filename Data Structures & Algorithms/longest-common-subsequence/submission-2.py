class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dic = {}

        def dfs(i, j):
            if (i, j) in dic:
                return dic[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                dic[(i, j)] = 1 + dfs(i+1, j+1)
                return dic[(i, j)]
            dic[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
            return dic[(i, j)]
            
        return dfs(0, 0)