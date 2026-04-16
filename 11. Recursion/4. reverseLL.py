# Reverse a Linked List using Recrusion

def reverseLL(head):
    if(head is None or head.next is None):
        return head
    
    new_head = reverseLL(head.next)

    head.next.next = head
    head.next = None

    return new_head

    

    



