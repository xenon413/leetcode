class Solution 
{
public:
    bool isValid(string s) 
    {
        stack<char> Stack;
        for (char i : s)
        {
            switch (i)
            {
            case ')':
                if ((! Stack.empty()) && Stack.top() == '(')
                    Stack.pop();
                else
                    return false;
                break;
            case ']':
                if ((!Stack.empty()) && Stack.top() == '[')
                    Stack.pop();
                else
                    return false;
                break;
            case '}':
                if ((!Stack.empty()) && Stack.top() == '{')
                    Stack.pop();
                else
                    return false;
                break;
            default:
                Stack.push(i);
            }
        }
        if (Stack.empty())
            return true;
        return false;
    }
};