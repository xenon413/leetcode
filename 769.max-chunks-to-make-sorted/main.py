class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i = 0
        cnt = 0
        pairs = []
        for i in range(len(arr)):
            new_pair = [min(i, arr[i]), max(i, arr[i])]
            # check if fits
            j = 0
            while j < len(pairs):
                if pairs[j][0] <= new_pair[0] <= pairs[j][1]:
                    pairs[j][1] = max(pairs[j][1], new_pair[1])
                    break

                elif pairs[j][0] <= new_pair[1] <= pairs[j][1]:
                    pairs[j][0] = min(pairs[j][0], new_pair[0])
                    break
                j+=1

            else:
                pairs.append(new_pair)

        return len(pairs)

            