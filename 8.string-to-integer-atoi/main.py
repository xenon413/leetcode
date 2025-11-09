class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        step = 1
        res = ""
        while i < len(s):
            if step == 1:
                if s[i] == " ":
                    i+=1
                else:
                    step+=1
            
            elif step == 2:
                if s[i] == "-":
                    i+=1
                    res += "-"
                
                elif s[i] == "+":
                    i+=1
                
                step += 1
            
            else:
                if s[i].isnumeric():
                    res += s[i]
                    i += 1
                else:
                    break
        if res == "" or res == "-":
            return 0
        res = int(res)
        if res > 2**31 -1:
            res = 2**31 -1
        elif res < -2**31:
            res = -2**31
        return res