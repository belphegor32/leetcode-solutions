class Solution:
    def evalRPN(self, tokens) -> int:

        # use stack and append values until you met an operator, if an operator is met we use it on the last two added values in the stack
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[-1]