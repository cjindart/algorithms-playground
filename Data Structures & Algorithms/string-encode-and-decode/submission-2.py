class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            n = len(s)
            result += str(n) + "#" + s
        return result
                
    # Given "5#Hello5#World" -> ["Hello", "World"]
    #        l
    #         r
    def decode(self, s: str) -> List[str]:
        result = []
        l, r = 0, 0

        while r < len(s):
            if s[r] == "#":
                n = int(s[l:r])
                word = s[r+1:r+1+n]
                result.append(word)
                l, r = r + n + 1, r + n + 1
            r += 1
        return result

                

            

        






        return []
