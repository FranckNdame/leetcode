#include <unordered_map>
#include <stack>
#include <vector>
class Solution
{
public:
    bool isValid(std::string s)
    {
        std::unordered_map<char, char> lookup{{')', '('}, {']', '['}, {'}', '{'}};
        std::stack<char> stack;

        for (char c : s)
        {
            std::string openBrackets = "({[";
            if (openBrackets.find(c) != std::string::npos)
            {
                stack.push(c);
            }
            else
            {
                if (stack.size() == 0)
                    return false;
                char opening = stack.top();
                stack.pop();
                if (opening != lookup[c])
                    return false;
            }
        }

        return stack.size() == 0;
    }
};