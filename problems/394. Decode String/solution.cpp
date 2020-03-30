
class Solution
{
public:
    // Optimal approach
    // Naive approach
    string decodeString(string s)
    {
        string decoded_str;
        int i(0), num(0);

        while (i < s.size())
        {
            num = 0;
            if (isDigit(s[i]))
            {
                while (isDigit(s[i]))
                    num = num * 10 + (int)s[i++] - 48;
                int length = getLength(i, s);
                for (int j = 0; j < num; j++)
                    decoded_str += decodeString(s.substr(i + 1, length));
                i += length + 1;
            }
            else
                decoded_str += s[i];
            i++;
        }

        return decoded_str;
    }

    int getLength(int start, string s)
    {
        int openBrackets(1);
        int length(-1), i(start + 1);

        while (openBrackets)
        {
            if (s[i] == '[')
                openBrackets++;
            if (s[i++] == ']')
                openBrackets--;
            length++;
        }
        return length;
    }

    bool isDigit(char c)
    {
        return 48 <= (int)c && (int)c < 58;
    }
};