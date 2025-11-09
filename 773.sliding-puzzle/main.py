class Solution:
    @staticmethod
    def check(cur) -> bool:
        if cur[1] != 1:
            return False
        elif cur[2] != 2:
            return False
        elif cur[3] != 3:
            return False
        elif cur[4] != 4:
            return False
        elif cur[5] != 5:
            return False
        elif cur[6] != 0:
            return False
        
        return True

    @staticmethod
    def swap(cur, zero_index, target_index):
        temp = cur.copy()
        temp[zero_index] = temp[target_index]
        temp[target_index] = 0
        temp["zero_pos"] = target_index
        return temp
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        record = []
        queue = []
        cur = {}
        #find positions to val
        for i in range(len(board[0])):
            cur[i+1] = board[0][i]
            cur[i+4] = board[1][i]
            if board[0][i] == 0:
                cur["zero_pos"] = i+1
            elif board[1][i] == 0:
                cur["zero_pos"] = i+4

        queue.append(cur)
        record.append(cur)
        cnt = 0
        while queue:
            new_queue = []
            # get all board where with n moves
            for cur in queue:
                # check if currect is the end
                if self.check(cur):
                    return cnt
                
                new_curs = []
                # update queue
                if cur["zero_pos"] == 1:
                    new_curs.append(self.swap(cur, 1, 2))
                    new_curs.append(self.swap(cur, 1, 4))

                elif cur["zero_pos"] == 2:
                    new_curs.append(self.swap(cur, 2, 1))
                    new_curs.append(self.swap(cur, 2, 3))
                    new_curs.append(self.swap(cur, 2, 5))

                elif cur["zero_pos"] == 3:
                    new_curs.append(self.swap(cur, 3, 2))
                    new_curs.append(self.swap(cur, 3, 6))
                    
                elif cur["zero_pos"] == 4:
                    new_curs.append(self.swap(cur, 4, 1))
                    new_curs.append(self.swap(cur, 4, 5))

                elif cur["zero_pos"] == 5:
                    new_curs.append(self.swap(cur, 5, 4))
                    new_curs.append(self.swap(cur, 5, 6))
                    new_curs.append(self.swap(cur, 5, 2))

                else:
                    new_curs.append(self.swap(cur, 6, 5))
                    new_curs.append(self.swap(cur, 6, 3))

                # check if in record
                # print(new_curs)
                for new_cur in new_curs:
                    if new_cur not in record:
                        record.append(new_cur)
                        new_queue.append(new_cur)

            # update queue
            queue = new_queue

            # clear new queue
            new_queue = []

            # update cnt
            cnt += 1
        return -1

