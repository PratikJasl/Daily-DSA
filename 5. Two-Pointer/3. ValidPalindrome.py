# 125. Valid Palindrome

# Approach: T:O(n) | S:O(1)
# Step1: Clean the string

def ValidPalindrome(s: str) -> bool:
    cleaned = "".join(char for char in s if char.isalnum()).lower()
    left = 0
    right = len(cleaned) - 1
    while(left < right):
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True