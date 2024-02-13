#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n == 0){
            return -1;
        }

        int l = 0;
        int r = n - 1;

        while(l <= r){
            int mid = floor((l + r) / 2);
            if(target == nums[mid]){
                return mid;
            }

            if(nums[l] <= nums[mid]){
                // if the target is greater than the middle and smaller than the smallest value in the current scope of bin search< then we look to the right, since the smaller value can only be to the right
                if(nums[mid] < target || target < nums[l]){
                    l = mid + 1;
                }
                else{
                    r = mid - 1;
                }
            }
            else{
                // if the target is smaller than the middle and larger than the right most value, we search left(since the smaller value can only be in the left now)
                if(target < nums[mid] || target > nums[r]){
                    r = mid - 1;
                }
                else{
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
};