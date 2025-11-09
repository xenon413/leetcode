class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        my_dict = defaultdict(int)
        for i in arr:
            if my_dict[i] > 0:
                return True
            
            if i%2 == 0:
                my_dict[i/2] +=1
            my_dict[i*2] += 1
        return False