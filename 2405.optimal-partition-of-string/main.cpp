class Solution {
public:
    int partitionString(string s) {
        int dp[26] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
        int cnt=1;
        for (int i = 0; i < s.size(); i++) {
            if (dp[s[i] - 97] != 0) {
                cnt++;
                for (int k = 0; k < 26; k++) {
                    dp[k] = 0;
                }
                dp[s[i] - 97] = 1;
            }
            else {
                dp[s[i] - 97] = 1;
            }
        }
        return cnt;
    }
};