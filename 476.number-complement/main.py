class Solution:
    def findComplement(self, num: int) -> int:
        num=str(bin(num))
        string=""
        for i in range(len(num[2:])):
            if num[i+2]=="0":
                string+="1"
            else:
                string+="0"
        string=int(string,2)
        return string;
