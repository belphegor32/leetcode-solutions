#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        if (nums.size() % 3 != 0)
            return vector<vector<int>>();

        sort(nums.begin(), nums.end());

        vector<vector<int>> res(nums.size() / 3, vector<int>(3));
        int groupInd = 0;

        for(int i = 0; i < nums.size(); i += 3){
            // # if after sorting the last elem - first elem (in current array) is greater than k, then the whole list is impossible to divide
            if(nums[i + 2] - nums[i] > k){
                return vector<vector<int>>();
            }
            else{
                res[groupInd] = { nums[i], nums[i + 1], nums[i + 2]};
                groupInd += 1;
            }
        }
        return res;
    }
};