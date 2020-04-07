class Solution
{
public:
    vector<int> pancakeSort(vector<int> &A)
    {
        vector<int> result;
        for (int i = 0; i < A.size(); i++)
        {
            if (!isUnsorted(A))
                break;
            int idx = 0;
            for (int j = 1; j < A.size() - i; j++)
            {
                if (A[j] > A[idx])
                    idx = j;
            }

            flip(A, idx + 1, result);
            flip(A, A.size() - i, result);
        }
        return result;
    }

    bool isUnsorted(vector<int> &A)
    {
        for (int i = 1; i < A.size(); i++)
        {
            if (A[i] < A[i - 1])
                return true;
        }
        return false;
    }

    void flip(vector<int> &A, int k, vector<int> &result)
    {
        result.push_back(k);
        int left(0), right(k - 1);
        while (left < right)
        {
            swap(A[left++], A[right--]);
        }
    }
};
