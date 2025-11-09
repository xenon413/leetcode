class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort(reverse=True)
        ans = []
        for i in spells:
            # init
            start = 0
            end = len(potions)-1
            pivot = (start + end)//2
            while True:
                # base case
                if i*potions[pivot] >= success:
                    start = pivot
                else:
                    end = pivot
                pivot = (start + end)//2

                # break point
                if pivot == start or pivot == end:
                    if i*potions[end] >= success:
                        ans.append(end+1)
                    elif i*potions[start] >= success:
                        ans.append(start+1)
                    else:
                        ans.append(start)
                        
                    break

                
        return ans