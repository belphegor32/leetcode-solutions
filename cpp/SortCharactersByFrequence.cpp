#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>


using namespace std;
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> count;
        string res = "";

        for(int i = 0; i < s.size(); i++){
            count[s[i]] += 1;
        }

        vector<char> sortedC;
        for (const auto& pair : count) {
            sortedC.push_back(pair.first);
        }

        sort(sortedC.begin(), sortedC.end(), [&](char a, char b) {
            return count[a] > count[b];
        });
        for(char c : sortedC){
            res += string(count[c], c);
        }

        return res;
    }
};