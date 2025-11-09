class Solution:
    def partitionString(self, s: str) -> int:
        sub = ""
        cnt = 1
        for i in s:
            if i in sub:#reset
                sub=""
                cnt+=1
            sub+=i
        return cnt