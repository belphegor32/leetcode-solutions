#include <iostream>
#include <unordered_map>
#include <vector>


using namespace std;
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        int res = 0;
        int l = 0;
        int r = 0;

        while(r < nums.size()){
            count[nums[r]] += 1;

            // if the element we just increased in hashmap is more than k, we need to remove the element we increased from the left side
            while(count[nums[r]] > k){
                count[nums[l]] -= 1;
                l += 1;
            }
            // res will be the max size of the window
            res = max(res, (r - l) + 1);
            r += 1;
        }
        return res;
    }
};