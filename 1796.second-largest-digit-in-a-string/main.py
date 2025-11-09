class Solution:
    def secondHighest(self, s: str) -> int:
        a = set()
        for i in s:
            if i.isdigit():
                a.add(i)

        a = list(a)
        a.sort()
        try:
            return int(a[-2])
        except:
            return -1