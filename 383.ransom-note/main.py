class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mlst = [0 for _ in range(26)]
        for i in magazine:
            mlst[ord(i) - 97] += 1
        for i in ransomNote:
            mlst[ord(i) - 97] -= 1
            if mlst[ord(i) - 97] <0:
                return False
        return True