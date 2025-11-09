
class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace("/","//")
        ans=eval(s)
        return ans;