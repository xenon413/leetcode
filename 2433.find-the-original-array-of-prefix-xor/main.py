class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #initialize
        ans = [pref[0]]
        pL = len(pref)
        index = 1

        #loop
        while(pL>len(ans)):
            
            #do xor 
            ans.append(pref[index-1] ^ pref[index])

            
            #add index
            index +=1
        return ans