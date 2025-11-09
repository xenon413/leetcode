#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<sstream>
#include<algorithm>
using namespace std;
class Solution 
{
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr)
    {
        vector<vector<int>>ans;
        sort(arr.begin(), arr.end());
        int distance = INT_MAX;
        for (int i = 0; i < arr.size()-1; i++)
        {
            int x = arr[i], y = arr[i + 1];
            if (distance > abs(x - y))
            {
                ans.clear();
                ans.push_back({ x,y });
                distance = abs(x - y);
            }
            else if (distance == abs(x - y))
                ans.push_back({ x,y });
        }
        return ans;
    }
};