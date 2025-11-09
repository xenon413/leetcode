class Solution:
    def longestPalindrome(self, s: str) -> str:
        queue = []
        ans = s[0]
        size = 1
        # get base
        for i in range(0, len(s)):
            start = i
            end1 = i+1
            end2 = i+2

            if end1<=len(s)-1 and s[start] == s[end1]:
                queue.append([start, end1])
                # replce
                if size < 2:
                    size = 2
                    ans = s[start:end1+1]
                
            
            if end2<=len(s)-1 and s[start] == s[end2]:
                queue.append([start, end2])
                if size < 3:
                    size = 3
                    ans = s[start:end2+1]

        # expand
        while queue:
            cur = queue.pop()
            start = cur[0] - 1
            end = cur[1] + 1
            while start > -1 and end < len(s):
                if s[start] == s[end]:
                    # replce
                    if size < end - start + 1:
                        size = end - start + 1
                        ans = s[start:end+1]
                else:
                    break
                start -= 1
                end += 1
                
        return ans
