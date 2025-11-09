#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string ans = "";
        int j = 0;
        for(int i=0;i<s.size();i++){
            if(j < spaces.size() && spaces[j] == i){
                ans += " ";
                j+=1; 
            }
                
            ans += s[i];
        }
        return ans;
    }
};