class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reorderll(head):
    slow = head
    fast = head

    # Step1: Place slow pointer at mid.
    while (fast and fast.next.next):
        slow = slow.next
    
    # Step2: Split the list.
    current = slow.next
    slow.next = None
    prev = None
    forw = None

    #Step3: Reverse the second half.
    while(current is not None):
        forw = current.next
        current.next = prev
        prev = current
        current = forw

    #Step4: Merge LL
    first = head
    second = prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next, second.next = second, temp1
        first, second = temp1, temp2

    