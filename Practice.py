def longestSubstring(s: list[str]) -> int:
    if not s:
        return 0
    
    n = len(s)
    seen = set()
    max_count = 0
    right = 0
    left = 0
    while(right < n):
        if(s[right] not in seen):
            seen.add(s[right])
            right += 1
            max_count = max(len(seen), max_count)
        else:
            seen.clear()
        print(seen)
    return max_count


print(longestSubstring('dvdf'))