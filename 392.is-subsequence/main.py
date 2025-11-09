class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        lens = len(s)
        lent = len(t)
        if lens > lent:
            return False
        while i < lens and lent-j >= lens-i:
            if s[i] == t[j]:
                i += 1
            j += 1
        if i >= lens:
            return True
        return False