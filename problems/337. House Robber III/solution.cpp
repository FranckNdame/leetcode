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
    int rob(TreeNode *root)
    {
        int l, r;
        return rob(root, l, r);
    }

    int rob(TreeNode *node, int &left, int &right)
    {
        if (!node)
            return 0;
        int leftL, leftR, rightL, rightR;
        leftL = leftR = rightL = rightR = 0;

        left = rob(node->left, leftL, leftR);
        right = rob(node->right, rightL, rightR);

        return max(node->val + leftL + leftR + rightL + rightR, left + right);
    }
};