#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        
        stack<float> stack;
        vector<pair<int, float>> fleet;
         
        for(int i = 0; i < position.size(); i++)
            fleet.push_back({ position[i], float(target - position[i]) / speed[i] });
        
        sort(fleet.begin(), fleet.end());
                   
        
        for(int i = 0; i < position.size(); i++){
            float carTime = fleet[i].second;
         
            while(stack.size() && (carTime >= stack.top()))
                stack.pop();
            
            stack.push(carTime);
        }
        
        return stack.size();
    }
};