#include <iostream> 
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<pair<int, int>> stack;
        vector<int> result(n);
        
        for (int i = 0; i < n; i++) {
            int currDay = i;
            int currTemp = temperatures[i];
            
            while (!stack.empty() && stack.top().second < currTemp) {
                int prevDay = stack.top().first;
                int prevTemp = stack.top().second;
                stack.pop();
                
                result[prevDay] = currDay - prevDay;
            }
            
            stack.push({currDay, currTemp});
        }
        
        return result;
    }
};