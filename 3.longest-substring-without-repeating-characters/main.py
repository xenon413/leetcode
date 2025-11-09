class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        i, j = 0, 1
        my_dict = defaultdict(int)
        my_dict[s[i]] +=1
        imax = 0

        while j < len(s):
            
            # if f[j] not the only letter
            while my_dict[s[j]] != 0:
                my_dict[s[i]] -= 1
                i+=1
            
            my_dict[s[j]] +=1
            imax = max(j-i, imax)
            j+=1
        return imax + 1