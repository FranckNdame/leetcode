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
    int index = 0;

    TreeNode *bstFromPreorder(vector<int> &nums, int hi = INT_MAX, int lo = INT_MIN)
    {
        if (this->index >= nums.size() || nums[this->index] >= hi || nums[this->index] <= lo)
            return nullptr;
        TreeNode *node = new TreeNode(nums[this->index++]);
        node->left = bstFromPreorder(nums, node->val, lo);
        node->right = bstFromPreorder(nums, hi, node->val);
        return node;
    }
};