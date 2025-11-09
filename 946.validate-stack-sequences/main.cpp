class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        vector<int>stack;
        int cnt = 0;
        for (int i : pushed)
        {
            stack.push_back(i);
            while (!stack.empty()&&stack.back() == popped[cnt])
            {
                stack.pop_back();
                cnt++;
            }
        }
        if (stack.empty())
            return true;
        return false;
    }
};