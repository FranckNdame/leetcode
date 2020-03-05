class Solution
{
public:
    int countPrimes(int n)
    {
        int count = 0;
        vector<int> visited(n);
        for (int i = 0; i < n; i++)
            visited[i] = false;

        for (unsigned long i = 2; i < n; i++)
        {
            if (visited[i] == true)
                continue;
            count++;
            unsigned long temp = i * i;
            while (temp < n)
            {
                visited[temp] = true;
                temp += i;
            }
        }

        return count;
    }
};