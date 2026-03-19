class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"} # Using a Set is slightly faster for lookups!

        for token in tokens:
            if token in operators:
                # 1. Calculate the result (this helper pops the numbers for us)
                result = self.performOperation(stack, token)
                
                # 2. Push the result back onto the stack
                stack.append(result)
            else:
                # 3. If it's a number, convert it to an integer and push it
                stack.append(int(token))
        
        # At the end, the only thing left in the stack is our final answer
        return stack.pop()

    # Added 'self' here!
    def performOperation(self, stack, operator) -> int:
        right_operand = stack.pop() 
        left_operand = stack.pop()  
    
        if operator == "+":
            return left_operand + right_operand
        elif operator == "-":
            return left_operand - right_operand
        elif operator == "*":
            return left_operand * right_operand
        elif operator == "/":
            return int(left_operand / right_operand)