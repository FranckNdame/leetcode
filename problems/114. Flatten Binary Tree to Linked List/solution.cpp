/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
    void flatten(TreeNode *root)
    {
        if (root == nullptr)
            return;
        stack<TreeNode *> stack;
        TreeNode *curr = root;
        if (curr->right)
            stack.push(curr->right);
        if (curr->left)
            stack.push(curr->left);

        while (stack.size())
        {
            TreeNode *node = stack.top();
            stack.pop();
            curr->left = nullptr;
            curr->right = node;
            if (node->right)
                stack.push(node->right);
            if (node->left)
                stack.push(node->left);
            curr = node;
        }
    }
};