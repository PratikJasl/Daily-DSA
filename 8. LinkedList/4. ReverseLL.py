# 206. Reverse Linked List:

# Approach: Brute Force: Using a List
# BIG O: T:O(n), s:O(n)
def reverseList(self, head):
    values = []
    temp = head
    # Step1: Store all values in a list.
    while(temp is not None):
        values.append(temp.val)
        temp = temp.next
    print("Array Created:", values)

    # Step2: Use the list to reverse the linked list.
    i = len(values) - 1
    temp = head
    while(temp is not None and i >= 0):
        temp.val = values[i]
        temp = temp.next
        i -= 1
    return head

#Appraoch: Optimal 
# Time Complexity: O(n) | S(1)
# Using 3 pointers 
# Step1: Create 3 pointers. (previous, current, next)
# Step2: Current starts at head, next starts at current.next and previous start at Null.
# Step3: Iterate through the list and make the connections backward.
# Step4: Point the head to prev, to make new head.

def reverseList(head):
    current = head
    prev = None
    next = None

    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev

    return head
    