class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        stack = []
        ans = 0
        for i in s:
            if stack and stack[-1]<d[i]:
                ans -= stack.pop()
                ans += d[i]
            
            else:
                stack.append(d[i])

        ans += sum(stack)
        return ans
                