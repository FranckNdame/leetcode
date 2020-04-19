class Solution
{
public:
    bool checkValidString(string s)
    {
        stack<int> open, stars;
        for (int i = 0; i < s.size(); i++)
        {
            switch (s[i])
            {
            case '(':
                open.push(i);
                break;
            case '*':
                stars.push(i);
                break;
            default:
                if (open.empty() && stars.empty())
                    return false;
                if (open.empty())
                    stars.pop();
                else
                    open.pop();
            }
        }
        while (!open.empty())
        {
            if (stars.empty() || open.top() > stars.top())
                return false;
            stars.pop();
            open.pop();
        }

        return true;
    }
};
