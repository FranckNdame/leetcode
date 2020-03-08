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
    int maxDepth(TreeNode *root)
    {
        int result = 0;
        dfs(root, result, 1);
        return result;
    }

    void dfs(TreeNode *node, int &result, int currDepth)
    {
        if (!node)
        {
            result = max(result, currDepth - 1);
            return;
        }

        dfs(node->left, result, currDepth + 1);
        dfs(node->right, result, currDepth + 1);
    }
};