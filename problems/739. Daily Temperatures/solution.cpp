class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &T)
    {
        stack<pair<int, int>> stack;
        vector<int> result(T.size(), 0);

        for (int i = T.size() - 1; i >= 0; i--)
        {
            while (!stack.empty() && T[i] >= stack.top().first)
                stack.pop();
            if (!stack.empty())
                result[i] = stack.top().second - i;
            stack.push(make_pair(T[i], i));
        }

        return result;
    }
};
