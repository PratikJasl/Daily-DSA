//Leetcode: 141: Linked List Cycle

//Approach: O(N)
//Step1: Create a fast and slow pointer.
//Step2: Iterate through the linked list.
//Step3: make the fast pointer go faster.
//Step4: If fast pointer loops around and catches slow return true.

var hasCycle = function(head) {
    if(!head) return false;

    let fast = head;
    let slow = head;

    while(fast){
        if(!fast.next){
            return false
        }else{
            fast = fast.next.next;
            slow = slow.next;
        }

        if(fast === slow) return true;
    }
    return false;
};