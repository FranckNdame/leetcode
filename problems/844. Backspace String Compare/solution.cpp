class Solution
{
public:
    bool backspaceCompare(string S, string T)
    {
        vector<int> charCount(26, 0);

        int hashCount(0);
        for (int i = S.size() - 1; i >= 0; i--)
        {
            if (S[i] == '#')
                hashCount++;
            else if (!hashCount)
                charCount[S[i] - 'a']++;
            else
                hashCount--;
        }

        hashCount = 0;
        for (int j = T.size() - 1; j >= 0; j--)
        {
            if (T[j] == '#')
                hashCount++;
            else if (!hashCount)
                charCount[T[j] - 'a']--;
            else
                hashCount--;
        }

        for (int count : charCount)
        {
            if (count)
                return false;
        }

        return true;
    }
};