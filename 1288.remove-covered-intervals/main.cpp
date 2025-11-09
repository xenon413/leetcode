class Solution 
{
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) 
    {
        int imax = intervals.size();
        for (int i = 0; i < intervals.size() - 1; i++)
        {
            if (intervals[i][0] == -1)continue;
            for (int k = i+1; k < intervals.size(); k++)
            {
                if (intervals[k][0] == -1)continue;
                else if (intervals[i][0] <= intervals[k][0] && intervals[i][1] >= intervals[k][1])
                {
                    intervals[k][0] = intervals[k][1] = -1;
                    imax--;
                }
                else if (intervals[i][0] >= intervals[k][0] && intervals[i][1] <= intervals[k][1])
                {
                    intervals[i][0] = intervals[i][1] = -1;
                    imax--;
                    break;
                }
            }
        }
        return imax;
    }
};