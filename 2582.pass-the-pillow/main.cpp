class Solution {
public:
    int passThePillow(int n, int time) {
        if ((time/(n-1))%2==0)
            return 1+time%(n-1);
        return n-time%(n-1);
    }
};