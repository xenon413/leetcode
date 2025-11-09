class Solution {
public:
    int findComplement(int num) 
    {
        std::string r;
        while (num != 0) 
        {
            r = (num % 2 == 0 ? "0" : "1")+r;
            num /= 2;
        }
        //std::cout << r << '\n';
        for (unsigned int i=0;i<r.size();i++)
        {
            if (r[i] == '0')
                r[i] = '1';
            else
                r[i] = '0';
        }
        unsigned int m, sum=0,i=0;
        while (r != "0")
        {
            m = r.back()-48;
            r.pop_back();
            sum += m * pow(2, i);
            i++;
        }
        return sum;
    }
};