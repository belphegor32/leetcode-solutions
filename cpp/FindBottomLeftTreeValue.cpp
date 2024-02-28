#include <iostream>
#include <deque>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        deque<TreeNode*> q;
        q.push_front(root);
        TreeNode* node = NULL;

        while(!q.empty()){
            // we traverse tree level by level from right to left, so the last value in the q will be the asnwer
            node = q.back();
            q.pop_back();
            if(node->right != NULL){
                q.push_front(node->right);
            }
            if(node->left != NULL){
                q.push_front(node->left);
            }
        }
        return node->val;
    }
};