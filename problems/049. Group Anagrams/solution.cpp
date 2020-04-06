class Solution
{
public:
    // Approach One
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> map;

        for (string word : strs)
        {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            map[sortedWord].push_back(word);
        }

        for (auto it : map)
            result.push_back(it.second);
        return result;
    }

    // Approach Two
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> map;

        for (string word : strs)
        {
            string key;
            vector<int> counter(26, 0);
            for (char c : word)
                counter[c - 'a']++;
            for (int i = 0; i < 26; i++)
                key += "#" + to_string(counter[i]);
            map[key].push_back(word);
        }

        for (auto it : map)
            result.push_back(it.second);
        return result;
    }
};