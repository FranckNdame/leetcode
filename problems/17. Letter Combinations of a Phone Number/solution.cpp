class Solution
{
public:
    vector<string> letterCombinations(string digits)
    {
        if (digits.empty())
            return {};
        unordered_map<char, vector<char>> map({{'2', {'a', 'b', 'c'}},
                                               {'3', {'d', 'e', 'f'}},
                                               {'4', {'g', 'h', 'i'}},
                                               {'5', {'j', 'k', 'l'}},
                                               {'6', {'m', 'n', 'o'}},
                                               {'7', {'p', 'q', 'r', 's'}},
                                               {'8', {'t', 'u', 'v'}},
                                               {'9', {'w', 'x', 'y', 'z'}}});
        vector<string> result;
        getCombination(digits, result, map);
        return result;
    }

    void getCombination(string &digits, vector<string> &result, unordered_map<char, vector<char>> &map, int index = 0, string str = "")
    {
        if (index == digits.size())
        {
            result.push_back(str);
            return;
        }
        vector<char> letters = map[digits[index]];
        for (char letter : letters)
        {
            getCombination(digits, result, map, index + 1, str + letter);
        }
    }
};
