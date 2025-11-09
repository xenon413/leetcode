class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fL = len(flowerbed)
        
        #if no new flower
        if n<=0:
            return True
        #case len(flowerbed) == 1
        if fL == 1:
            temp = flowerbed[0]
            if temp == 1:
                if n>0:
                    return False
                return True
            else:
                if n>1:
                    return False
                return True
        #check left
        if flowerbed[1] == 0 and flowerbed[0] == 0:
            flowerbed[0] = 1
            n-=1
        
        #check right
        if flowerbed[fL-2] == 0 and flowerbed[fL-1] == 0:
            flowerbed[fL-1] = 1
            n-=1
        
        #loop check
        i=1
        while True:
            #break point 1
            if n<=0:
                return True
            
            #break point 2
            if i>=fL-1:
                return False
            
            #check left right and i
            if flowerbed[i+1] == 1:
                i+=3
            elif flowerbed[i] == 1:
                i+=2
            elif flowerbed[i-1] == 1:
                i+=1
            else:
                flowerbed[i]=1
                i += 2 
                n-=1
