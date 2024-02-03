#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// memoization with recursion solution
class Solution {
public:
    unordered_map<int, int> cache;
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        return rec(arr, 0, k);

    }

    int rec(vector<int> &arr, int i, int k){
        int n = arr.size();
        if(i >= n){
            return 0;
        }
        if(cache.count(i) != 0){
            return cache[i];
        }

        int max_elem = 0;
        int res = 0;
        for(int j = i; j < min(n, i + k); j++){
            max_elem = max(max_elem, arr[j]);
            int window_size = j - i + 1;
            res = max(res, max_elem * window_size + rec(arr, j + 1, k));
        }

        cache[i] = res;
        return res;
    }
};