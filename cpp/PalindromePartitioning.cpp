#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> cur;
        backtracking(s, 0, cur, res);
        return res;

    }
    void backtracking(string &s, int i, vector<string>& cur, vector<vector<string>>& res){

        int len = s.size();
        // if the index is out of bound we include cur substing
        if(i == len){
            res.push_back(cur);
        }
        else{
            for(int j = i; j < len; j++){
                // chech if the string is a palindrome
                if(isPalindrome(s, i, j)){
                    cur.push_back(s.substr(i, j - i + 1));
                    // run backtracking to find other substrings that start from the next index
                    backtracking(s, j + 1, cur, res);
                    cur.pop_back();
                }
            }
        }
    }
    // helper function
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            if (s[l++] != s[r--]) {
                return false;
            }
        }
        return true;
    }
};