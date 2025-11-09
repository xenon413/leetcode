class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        ans = 0
        for t in text:
            for b in brokenLetters:
                if b in t:
                    break

            else:
                ans += 1

        return ans