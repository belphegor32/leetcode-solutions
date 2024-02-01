#include <iostream> 
#include <stack>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack1;
        
        // use stack and append values until you met an operator, if an operator is met we use it on the last two added values in the stack
        for(int i = 0; i < tokens.size(); i++){
            if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/"){
                int val2 = stack1.top();
                stack1.pop();
                int val1 = stack1.top();
                stack1.pop();
                switch(tokens[i][0]){
                    case '+':
                        stack1.push(val1 + val2);
                        break;
                    case '*':
                        stack1.push(val1 * val2);
                        break;
                    case '-':
                        stack1.push(val1 - val2);
                        break;
                    case '/':
                        stack1.push(val1 / val2);
                        break;
                }
            }
            else{
                stack1.push(stoi(tokens[i]));
            }
        }
        return stack1.top();
    }
};