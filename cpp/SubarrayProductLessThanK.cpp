#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int res = 0;
        int l = 0;
        int r = 0;
        int cur_prod = 1;
        
        // use sliding window to track if current subarray is greater than k
        while(r < nums.size()){
            // increase current product
            cur_prod = cur_prod * nums[r];
            // if current product is greater than k, we remove values from the left until the product is less than k
            while(l <= r && cur_prod >= k){
                cur_prod = cur_prod / nums[l];
                l += 1;
            }

            // the number of subarrays in current window will be equal to the length of the window
            res += (r - l) + 1;
            r += 1;
        }
        return res;
    }
};