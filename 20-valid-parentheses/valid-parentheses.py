class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to store the mapping of opening and closing brackets
        brackets = {'(':')', '{':'}', '[':']'}
        
        # Stack/list to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the input string
        for i in s:
            # If the character is an opening bracket, push it onto the stack
            if i in brackets:
                stack.append(i)
            else:
                # If the stack is empty or the current closing bracket doesn't match
                # the corresponding opening bracket, return False
                if len(stack) == 0 or i != brackets[stack.pop()]:
                    return False
        
        # Check if there are any remaining opening brackets in the stack
        return len(stack) == 0