class Solution:
    def intToRoman(self, num: int) -> str:
        ans =''
        num = str(num)
        size = len(num)
        ten = ['M', 'C', 'X', 'I']  # pre9 - 3
        five = ['', 'D','L', 'V']  #4 - 8
        if size <3:
            ten_max = ten[-(size + 1)]
        else:
            ten_max = ten[0]
        ten = ten[-size:]
        five = five[-size:]
        for i, current in enumerate(num):
            current = int(current)
            if current <= 3:  # 0-3 III
                for _ in range(current):
                    ans += ten[i]
            elif current <=8:
                if current == 4:  # IV
                    ans = ans + ten[i] + five[i]
                else:
                    ans += five[i]
                    for _ in range(current - 5):  # simplfy
                        ans += ten[i]
            else:  # 9 IX
                ans += ten[i]
                if i == 0:
                    ans += ten_max
                else:
                    ans += ten[i-1]
        return ans