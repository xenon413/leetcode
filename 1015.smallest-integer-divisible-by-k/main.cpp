class Solution 
{
public:
    int smallestRepunitDivByK(int k) 
    {
        long long int n = 1;
        int cnt = 1;
        if (k % 2 == 0||k%5==0)
            return -1;
        else
        {
            while ( n % k != 0)
            {
                n = (n * 10 + 1)%k;
                cnt++;
            }   
        }
        return cnt;
    }
};