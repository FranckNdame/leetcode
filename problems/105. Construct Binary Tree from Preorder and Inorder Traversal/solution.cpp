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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        unordered_map<int, int> preOrderMap, inOrderMap;
        int rootIdx(0);
        for (int i = 0; i < preorder.size(); i++)
        {
            preOrderMap[preorder[i]] = i;
            inOrderMap[inorder[i]] = i;
        }
        return construct(rootIdx, 0, preorder.size() - 1, preorder, inorder, preOrderMap, inOrderMap);
    }

    TreeNode *construct(int &rootIdx, int left, int right, vector<int> &preorder, vector<int> &inorder, unordered_map<int, int> &preOrderMap, unordered_map<int, int> &inOrderMap)
    {
        if (left > right || rootIdx >= preorder.size())
            return NULL;
        int val = preorder[rootIdx++];
        TreeNode *root = new TreeNode(val);
        if (left == right)
            return root;
        int idx = inOrderMap[val];
        root->left = construct(rootIdx, left, idx - 1, preorder, inorder, preOrderMap, inOrderMap);
        root->right = construct(rootIdx, idx + 1, right, preorder, inorder, preOrderMap, inOrderMap);

        return root;
    }
};