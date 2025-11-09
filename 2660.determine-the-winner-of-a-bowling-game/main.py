class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        double1 = 0
        double2 = 0

        for i in range(len(player1)):

            add1 = player1[i]
            add2 = player2[i]
            if double1:
                add1*=2
                double1 -= 1

            if double2:
                add2*=2
                double2 -= 1

            sum1 += add1
            sum2 += add2

            if player1[i] == 10:
                double1 = 2

            if player2[i] == 10:
                double2 = 2

        if sum1 > sum2:
            return 1
        
        if sum2 > sum1:
            return 2
        
        if sum2 == sum1:
            return 0