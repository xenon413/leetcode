class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_time = events[0][1]
        button = events[0][0]
        for i in range(len(events)-1):
            cur_time = events[i+1][1]-events[i][1]
            if cur_time > max_time:
                max_time = cur_time
                button = events[i+1][0]

            if cur_time == max_time:
                button = min(button, events[i+1][0])

        return button