#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        // sorting deals with this condion a1 <= a2 <= a3 <= ... <= ak (every next side should be >= than the prev)
        sort(nums.begin(), nums.end());

        long long maxTotal = -1;
        long long total = 0;

        for(int i = 0; i < nums.size(); i++){

            // checks the condition a1 + a2 + a3 + ... + ak-1 > ak (the longest side should be shorter than all prev sides combined)
            if(total > nums[i]){
                maxTotal = total + nums[i];
            }
            total += nums[i];
        }
        return maxTotal;
    }
};