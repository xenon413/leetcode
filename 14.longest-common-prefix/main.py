class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        re = []
        i = 0
        while True:
            d = set()
            for s in strs:
                if i < len(s):
                    d.add(s[i])
                else:
                    break
            else:
                if len(d) == 1:
                    re.append(list(d)[0])
                    i+=1
                    continue
                else:
                    break
            break
        return "".join(re)