#include <iostream>
#include <vector>


using namespace std;
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res(n + 1, 0);
        int offset = 1;

        for(int i = 1; i <= n; i ++){
            if(offset * 2 == i){
                offset = i;
            }
            res[i] = 1 + res[i - offset];
        }

        return res;
    }
};