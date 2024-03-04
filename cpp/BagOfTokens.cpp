#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        // sort the vector, so we know which tokens are better to play up and which are better to play down
        sort(tokens.begin(), tokens.end());
        int res = 0;
        int cur_score = 0;
        int l = 0;
        int r = tokens.size() - 1;
        
        while(l <= r){
            // we play the smallest tokens possible face up
            if(power >= tokens[l]){
                power -= tokens[l];
                l += 1;
                cur_score += 1;
                res = max(res, cur_score);
            }
            // and then play the biggest tokens face down to gain power
            else if(cur_score > 0){
                power += tokens[r];
                cur_score -= 1;
                r -= 1;
            }
            else{
                break;
            }
            }
        return res;
        }
};