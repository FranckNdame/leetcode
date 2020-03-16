class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        if (!digits.size())
            return digits;
        int i = digits.size() - 1, carry = 1;

        while (i >= 0)
        {
            if (!carry)
                break;
            digits[i] += carry;
            carry = 0;
            if (digits[i] == 10)
            {
                digits[i] = 0;
                if (i == 0)
                    digits.insert(digits.begin(), 1);
                carry++;
            }
            i--;
        }

        return digits;
    }
};
