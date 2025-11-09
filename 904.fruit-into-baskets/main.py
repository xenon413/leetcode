class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        size = len(fruits)
        if size <= 2:
            return size
        
        i = 0
        j = 0 # next start
        num = 2
        while True:
            i = j
            cnt = 0
            if i >= size-2:
                break

            first = fruits[i]
            cnt += 1

            # check next
            while i+1<size and fruits[i+1] == first:
                cnt += 1
                i += 1
                j += 1

            if i+1<size:
                i += 1
                j += 1
                cnt += 1
                second = fruits[i]

                # check next
                while i+1<size and (fruits[i+1] == second or fruits[i+1] == first):
                    cnt += 1
                    i += 1
                    
            num = max(num, cnt)
            if num == size:
                return num
        return num 