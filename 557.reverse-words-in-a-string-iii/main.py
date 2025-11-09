class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        ans = ""
        for i in lst:
            k = i[::-1]
            ans += k+' '
        return ans[0:-1]