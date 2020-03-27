class Solution
{
public:
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        vector<vector<int>> result;
        vector<int> combination;
        sort(candidates.begin(), candidates.end());
        helper(candidates, target, 0, combination, result);
        return result;
    }

    void helper(vector<int> &candidates, int target, int start, vector<int> &combination, vector<vector<int>> &result)
    {
        if (target < 0)
            return;
        else if (target == 0)
            result.push_back(combination);
        else
        {
            for (int i = start; i < candidates.size() && candidates[i] <= target; i++)
            {
                combination.push_back(candidates[i]);
                helper(candidates, target - candidates[i], i, combination, result);
                combination.pop_back();
            }
        }
    }
};
