# 21. Merge Two Sorted Lists


# Approach: Brute Force using List and sorting
# BIg-O:  T(NlogN) | S:O(N)
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Step1: Form a sorted lists from both ll.
    values = []
    temp1 = list1
    while(temp1 is not None):
        values.append(temp1.val)
        temp1 = temp1.next
    temp2 = list2
    while(temp2 is not None):
        values.append(temp2.val)
        temp2 = temp2.next
    values.sort()

    if not values:
        return None
    
    # Step2: From a new ll from values.
    n = len(values)
    head = ListNode(values[0])
    for i in range(1, n):
        new_node = ListNode(values[i])
        if(head.next is None):
            head.next = new_node
            temp = new_node
        else:
            temp.next = new_node
            temp = new_node
    
    return head

# Appoach: Optimal
# BigO: T:O(N) | S:O(1)
# Use two pointers
def mergeTwoLists(list1, list2):
    dummy = ListNode(-1)
    current = dummy
        
    # While both lists have nodes, compare and attach the smaller one
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If one list is longer, attach the rest of it
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
        
    return dummy.next