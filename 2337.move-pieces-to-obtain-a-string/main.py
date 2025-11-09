class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i=j=0
        slen = len(start)
        tlen = len(target)

        while i < slen and j < tlen:
            if start[i] == "_":
                i += 1
                continue

            if target[j] == "_":
                j += 1
                continue

            if start[i] != target[j]:
                return False

            elif start[i] == target[j] == "L" and j > i:
                return False
            
            elif start[i] == target[j] == "R" and j < i:
                return False
            
            else:
                i += 1
                j += 1
        while i < slen:
            if start[i] != "_":
                return False
            i+=1
        while j < slen:
            if target[j] != "_":
                return False
            j+=1
            
        return True