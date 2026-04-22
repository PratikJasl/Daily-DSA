def solve_problem(input_data):
    results = []
    # Place holders just for notation purpose no function.
    def is_goal_reached():
        pass
    def is_valid():
        pass
    
    def backtrack(path, options):
        # 1. Goal: Check if we have a complete/valid solution
        if is_goal_reached(path):
            results.append(path[:]) # Append a COPY of the path
            return
            
        # 2. Choices: Loop through all possible next steps
        for choice in options:
            # 3. Constraints: Should we skip this choice?
            if not is_valid(choice):
                continue
                
            # 4. Action / Undo
            path.append(choice)      # ACTION: Make the choice
            backtrack(path, options) # RECURSE: Explore down this path
            path.pop()               # UNDO: Backtrack to try the next choice
            
    backtrack([], input_data)
    return results

