/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        stack<TreeNode*> Stack;
        Stack.push(root); Stack.push(root);
        
        while (Stack.size() > 0) 
        {
            TreeNode* a = Stack.top(); Stack.pop();
            TreeNode* b = Stack.top(); Stack.pop();
            
            if (a->val != b->val) return false;
            
            if (a->left || b->right) {
                if (!(a->left && b->right)) return false;
                Stack.push(a->left); Stack.push(b->right);
            }
            
            if (a->right || b->left) {
                if (!(a->right && b->left)) return false;
                Stack.push(a->right); Stack.push(b->left);
            }
        }
        
        return true;
        
    }
};