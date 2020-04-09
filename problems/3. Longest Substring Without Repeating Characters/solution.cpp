class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> map;
        int maxLength(0), start(0);

        for (int i = 0; i < s.size(); i++)
        {
            if (map.find(s[i]) != map.end())
            {
                start = max(start, map[s[i]] + 1);
            }

            maxLength = max(maxLength, i - start + 1);
            map[s[i]] = i;
        }

        return maxLength;
    }
};