#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        // last group cant be created if the size of hand is not divisible by group size
        if(n % groupSize != 0){
            return false;
        }

        unordered_map<int, int> countMap;
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for(int i = 0; i < n; i++){
            countMap[hand[i]] += 1;
        }
        for(auto h : countMap){
            minHeap.push(h.first);
        }
        while(!minHeap.empty()){
            int top = minHeap.top();

            for(int i = top; i < top + groupSize; i++){
                // if the key is not in hashMap we return false since we cant create a group
                if(!(countMap.count(i))){
                    return false;
                }
                countMap[i] -= 1;
                if(countMap[i] == 0){
                    // we can only pop the value if its the smallest value in the heap, which is always on top in the minHeap
                    if(i != minHeap.top()){
                        return false;
                    }
                    minHeap.pop();
                }
            }
        }
        return true;
    }
};