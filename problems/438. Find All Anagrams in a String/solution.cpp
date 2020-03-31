class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        if (p.size() > s.size())
            return {};
        vector<int> freq(26, 0), result;
        for (char c : p)
            freq[c - 'a']++;
        int left(0), right(0), count(p.size());
        while (right < s.size())
        {
            if (freq[s[right++] - 'a']-- > 0)
                count--;
            if (count == 0)
                result.push_back(left);
            if (right - left == p.size() && freq[s[left++] - 'a']++ >= 0)
                count++;
        }
        return result;
    }
};
