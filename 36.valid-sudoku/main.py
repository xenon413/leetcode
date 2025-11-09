class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):# row
            lst = [k[i] for k in board if k[i] != '.']
            if len(board[i]) - board[i].count('.') + 1  > len(set(board[i])):
                return False
            if len(lst) > len(set(lst)):
                return False
            
        for i in range(1, 10, 3):
            for k in range(1, 10, 3):
                dp = [False for _ in range(9)]
                for j in range(-1, 2, 1):
                    for q in range(-1, 2, 1):
                        index = board[i + j][k + q]
                        if index != '.':
                            index = int(index) - 1
                            if dp[index]:
                                return False # not Valid
                            else:
                                dp[index] = True
        return True