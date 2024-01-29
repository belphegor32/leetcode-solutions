#include <iostream> 
#include <stack>
using namespace std;
class MyQueue {
public:
    stack<int> stack1;
    stack<int> stack2; 
    MyQueue() {
        
    }
    
    void push(int x) {
        // we only push to stack1, then values will be moved to stack 2 if needed
        stack1.push(x); 
    }
    
    int pop() {
        // if there are no values in stack2 we move all values from stack1 to it
        if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int s = stack2.top();
        stack2.pop();
        return s;
    }
    
    int peek() {
        // if there are no values in stack2 we move all values from stack1 to it
                if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        return stack2.top();
    }
    
    bool empty() {
        // if the max length of both stacks is 0, we return true, else false
        return max(stack1.size(), stack2.size()) == 0;
    }
};