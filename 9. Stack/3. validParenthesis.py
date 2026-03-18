# Step 1: Create a stack and map.
# Step 2: In the map, add combination of al closing backets to their opening.
# Step 3: Iterate through the string, if the char is in map, its a closing bracket.
# Step 4: Check if the closing bracket has an opening inside stack.
# Step 5: If you get an opening bracket add it to stack.

def validParanthesis(s: str):
    stack = []
    closeToOpen = { ')' : '(', ']' : '[', '}' : '{'}

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
        
    if(len(stack) == 0):
        return True
    else:
        return False