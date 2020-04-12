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
    typedef vector<TreeNode *> NodePath;
    vector<NodePath> paths;

public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        NodePath temp_path;
        GetPaths(root, p, q, temp_path);
        NodePath p_path = this->paths[0];
        NodePath q_path = this->paths[1];
        int i = min(p_path.size(), q_path.size()) - 1;
        while (p_path[i] != q_path[i])
            i--;
        return p_path[i];
    }

    void GetPaths(TreeNode *root, TreeNode *p, TreeNode *q, NodePath &path)
    {
        if (root == nullptr)
            return;
        path.push_back(root);
        if (root == p || root == q)
            this->paths.push_back(path);
        GetPaths(root->left, p, q, path);
        GetPaths(root->right, p, q, path);
        path.pop_back();
    }
};