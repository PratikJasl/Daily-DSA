# LeetCode: 739 Daily Temperatures

# Brute Force: O(n^2)
# Using two pointers slow and fast.

def dailyTemperatures(temperatures) -> list[int]:
    n = len(temperatures)
    output = []

    for slow in range(n):
        fast = slow + 1
        count = 0

        while(fast < n):
            count += 1
            if(temperatures[fast] > temperatures[slow]):
                break
            else:
                fast += 1
            
        if(fast >=n or temperatures[fast] < temperatures[slow]):
            output.append(0)
        else:
            output.append(count)
        
    return output

# Optimum Solution: Using Stack (Monotonic stack)
# Step1: Create an output array and fill it wi  th zero's.
# Step2: Create a stack which stores a pair [temp, index].
# Step3: When we encounter a temp we store its temp and index in stack.
# Step4: Next if we encounter a temp greater than our top of stack temp. We pop our stack and update output.

def dailyTemp(temperatures: list[int]) -> list[int]:
    output = [0] *len(temperatures)
    stack = [] #[temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            output[stackIndex] = (i - stackIndex)
        stack.append([temp, i])
    
    return output

