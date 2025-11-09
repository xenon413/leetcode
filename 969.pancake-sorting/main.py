class Solution:
    def pancakeSort(self, arr ):
        k = []
        end = len(arr)-1

        while True:
            # break point
            if end == 0:
                break

            # check end 
            if arr[end] == end+1:
                end -= 1
                continue

            max_num = -1
            index = -1
            # find max
            for i in range(end+1):
                if max_num < arr[i]:
                    max_num = arr[i]
                    index = i
                
            # flip front 
            if index != 0:
                arr[0:index+1] = arr[index::-1]
                k.append(index+1)

            # flip back
            arr[0:end+1] = arr[end::-1]
            k.append(end+1)

        return k