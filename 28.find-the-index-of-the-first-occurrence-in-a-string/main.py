class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack or needle == '':
            return -1
        else:
            return haystack.index(needle)

