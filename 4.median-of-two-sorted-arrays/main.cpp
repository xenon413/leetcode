class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    {
        double ans=0;
        for (int i : nums2)
            nums1.push_back(i);
        sort(nums1.begin(), nums1.end());
        if (nums1.size() % 2 == 1)
        {
            ans = nums1[(nums1.size() + 1) / 2 - 1];
        }
        else
        {
            ans = (nums1[nums1.size() / 2 - 1] + nums1[nums1.size() / 2]);
            ans /= 2;
        }
        return ans;
    }
};