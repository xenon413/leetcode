#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& num, int target) 
    {
        vector<int>out;
        for (int i = 0; i < num.size()-1; i++)
        {
            for (int k = i+1; k < num.size(); k++)
            {
                if (num[i] + num[k] == target)
                {
                    out.push_back(i);
                    out.push_back(k);
                    return out;
                }
            }
           
        }
        return out;
    }
};