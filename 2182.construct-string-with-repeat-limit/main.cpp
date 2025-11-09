#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        // init dp
        int repeats[26];
        for(int i=0;i<26;i++) repeats[i] = 0;

        // count repeat
        for(int i=0;i<s.size();i++) repeats[s[i]-97] += 1;

        // generate output
        string ans = "";
        int j = 24;
        int i = 25;
        while(i>=0){
            if(repeatLimit >= repeats[i]) {
                for(int k=0;k<repeats[i];k++) ans += i+97;
                i--;
            }
            else{
                // add to repeatlimint
                for(int k=0;k<repeatLimit;k++) ans += i+97;
                
                repeats[i] -= repeatLimit;

                j = min(j, i - 1);
                while(1){
                    if(j<0) break;

                    if(repeats[j] == 0) j--;

                    else{
                        ans += j+97;
                        repeats[j]--;
                        break;
                    }
                }
                if(j<0) break;
            }
        }
        return ans;
    }
};