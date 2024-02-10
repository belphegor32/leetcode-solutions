#include <iostream>


using namespace std;
class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        for(int i = 0; i < s.size(); i++){
            int l = i;
            int r = i;

            // count odd size palindromes
            while(l >= 0 && r < s.size() && s[l] == s[r]){
                res += 1;
                l -= 1;
                r += 1;
            }
            l = i;
            r = i + 1;
            // count even size palindromes
            while(l >= 0 && r < s.size() && s[l] == s[r]){
                res += 1;
                l -= 1;
                r += 1;
            }
        }
        return res;
    }
};