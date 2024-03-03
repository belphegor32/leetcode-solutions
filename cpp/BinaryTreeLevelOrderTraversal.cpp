#include <iostream>
#include <vector>
#include <deque>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        deque<TreeNode*> q;
        q.push_front(root);
        while(!q.empty()){
            int qLen = q.size();
            vector<int> level;
            for(int i = 0; i < qLen; i++){
                TreeNode* node = q.back();
                q.pop_back();
                if(node != NULL){
                    level.push_back(node->val);
                    q.push_front(node->left);
                    q.push_front(node->right);
                }
            }
            if(!level.empty()){
                res.push_back(level);
            }
        }
        return res;
    }
};