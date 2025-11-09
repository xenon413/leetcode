struct Data
{
    vector<int>xy = {};
    int distance = 0;
};
bool cmp(Data a, Data b)
{
    if (a.distance != b.distance)
        return a.distance < b.distance;
    return 0;
}
class Solution {
public:


    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) 
    {
        Data pro;
        vector<Data>data;
        vector<vector<int>>ans;
        for (vector<int>i : points)
        {
            pro.xy = i;
            pro.distance = i[0] * i[0] + i[1] * i[1];
            data.push_back(pro);
            //x * x + y * y;
        }
        sort(data.begin(),data.end(), cmp);

        for (int i = 0; i < k; i++)
            ans.push_back(data[i].xy);
        return ans;
    }
};