#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>


using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> h;

        for(int i = 0; i < strs.size(); i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            h[s].push_back(strs[i]);
        }
        vector<vector<string>> res;
        
        for(auto p : h){
            res.push_back(p.second);
        }
        return res;
    }
};