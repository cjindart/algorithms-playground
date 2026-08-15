class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            n = str(len(s))
            ret += n + "#" + s

        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        cur_start = 0

        while i < len(s):
            if s[i] == "#":
                n = int(s[cur_start:i])
                cur_start = i+1
                ret.append(s[cur_start:cur_start + n])
                i, cur_start = cur_start + n, cur_start + n
            i += 1
        
        return ret



