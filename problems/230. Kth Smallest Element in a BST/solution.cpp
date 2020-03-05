class Solution
{
public:
    int kthSmallest(TreeNode *root, int k)
    {
        if (root == NULL)
            return -1;
        std::vector<int> inOrder;
        getElements(root, inOrder);
        return inOrder[k - 1];
    }

    void getElements(TreeNode *node, std::vector<int> &arr)
    {
        if (node == NULL)
            return;
        getElements(node->left, arr);
        arr.push_back(node->val);
        getElements(node->right, arr);
    }
};