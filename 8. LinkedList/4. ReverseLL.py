# 206. Reverse Linked List:

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