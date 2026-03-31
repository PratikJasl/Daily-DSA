# Leet Code: 933: Number of Recent Calls

# Approach: Using Queue
# Step 1: Add new item to queue when ping.
# Step 2: Check if the first element is in the range (t-3000)
# Step 3: If not in range remove first till in range.
# Step 4: Return len queue.

class RecentCounter:
    def __init__(self):
        self.items = []

    def ping(self, t: int) -> int:
        self.items.append(t)
        while self.items[0] < t - 3000:
            self.items.pop(0)
        return len(self.items)