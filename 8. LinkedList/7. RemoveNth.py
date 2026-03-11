def removeNthFromEnd(self, head, n: int):
        # Step1: Calculate length of LL
        ll_length = 0
        temp = head
        while(temp is not None):
            ll_length += 1
            temp = temp.next
        print('Length of LL', ll_length)

        if(ll_length <= 1):
            return None
        
        # Step2: Calcuate when to stop.
        stop = (ll_length - n) + 1
        print('stop at', stop)

        # Step3: remove the element.
        step = 0
        temp1 = head
        prev = temp1
        if(stop == 1): #Remove 1st
            head = temp1.next
        while(temp1 is not None): #Remove from between
            step += 1
            if(step == stop):
                prev.next = temp1.next
            else:
                prev = temp1
                temp1 = temp1.next

        return head