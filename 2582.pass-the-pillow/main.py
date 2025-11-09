class Solution(object):
    def passThePillow(self, n, time):
        n-=1
        r = time%n
        d = time//n
        if d%2==0:
            return 1+r
        else:
            return n-r+1
        