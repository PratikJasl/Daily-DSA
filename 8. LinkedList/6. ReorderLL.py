# 143. Reorder List

# Optimal Solution
# Step1: Create two pointer fast and slow.
# Step2: Move the slow point 1 node and the fast pointer 2 nodes. This will place slow mointer in the middle.
# Step3: Split the list in two halves from slow(mid)
# Step4: Reverse the second half of the list.
# Step5: Merge the two lists together.
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def reorderList(self, head: ListNode) -> None:
    slow = head
    fast = head

    # Step1: Find middle of the list
    while(fast and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
    
    # Step2: Slipt the list in two halves
    second = slow.next
    slow.next = None
    node = None

    # Step3: Reverse the second half of ll.
    while second:
        temp = second.next
        second.next = node
        