class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        len1 = len(str1)
        len2 = len(str2)
        if len2 > len1:
            return False
        
        
        for k in range(len1):
            if str1[k] == str2[i] or chr((ord(str1[k])-97+1)%26+97) == str2[i]:
                i+=1
            if i >= len2:
                return True
            
            if len1-k < len2-i:
                break
        return False