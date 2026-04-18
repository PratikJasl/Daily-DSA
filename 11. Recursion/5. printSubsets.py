def print_subsets(arr, index=0, current_subset=[]):
    # Base Case: If we've considered all elements, print the current subset
    if index == len(arr):
        print(current_subset)
        return
    
    # Recursive Call 1: Include the current element
    print_subsets(arr, index + 1, current_subset + [arr[index]])
    
    # Recursive Call 2: Exclude the current element
    print_subsets(arr, index + 1, current_subset)


# Example Usage
my_array = [1, 2, 3]
print_subsets(my_array)
