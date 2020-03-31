class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<int> inDegrees(numCourses, 0);
        unordered_map<int, vector<int>> neighbours;
        stack<int> s;

        for (auto pre : prerequisites)
        {
            int u(pre[0]), v(pre[1]);
            neighbours[v].push_back(u);
            inDegrees[u]++;
        }

        populateStack(inDegrees, s);
        while (s.size())
        {
            int curr = s.top();
            s.pop();
            numCourses--;
            for (int neighbour : neighbours[curr])
                inDegrees[neighbour]--;
            populateStack(inDegrees, s);
        }
        return !numCourses;
    }

    void populateStack(vector<int> &inDegrees, stack<int> &s)
    {
        for (int i = 0; i < inDegrees.size(); i++)
        {
            if (!inDegrees[i])
            {
                s.push(i);
                inDegrees[i]--;
            }
        }
    }
};
