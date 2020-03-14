/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int depth(TreeNode *node, int &answer);
class Solution
{

public:
    int diameterOfBinaryTree(TreeNode *root)
    {
        int answer = 1;
        depth(root, answer);
        return answer - 1;
    }

    int depth(TreeNode *node, int &answer)
    {
        if (!node)
            return 0;
        int left = depth(node->left, answer);
        int right = depth(node->right, answer);
        answer = max(answer, left + right + 1);
        return max(left, right) + 1;
    }
};