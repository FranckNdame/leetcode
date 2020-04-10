class MinStack
{
public:
    vector<int> stack;
    vector<int> minStack;
    int currMin = INT_MAX;

    MinStack() {}

    void push(int x)
    {
        this->stack.push_back(x);
        this->currMin = min(currMin, x);
        this->minStack.push_back(currMin);
    }

    void pop()
    {
        if (this->stack.empty())
            return;
        this->stack.pop_back();
        this->minStack.pop_back();
        this->currMin = minStack.empty() ? INT_MAX : minStack.back();
    }

    int top()
    {
        return this->stack.back();
    }

    int getMin()
    {
        return this->minStack.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */