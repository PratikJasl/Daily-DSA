class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_begning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, None)
        if(self.head != None):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node 

    def insert_at_specific(self, data, position):
        new_node = Node(data)
        temp = self.head
        while(temp.data != position):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_element(self, data):
        temp = self.head
        prev = temp
        if(temp.data == data):
            self.head = temp.next
        while(temp.next != None):
            if(temp.data == data):
                prev.next = temp.next
                break
            else:
                prev = temp
                temp = temp.next
        if(temp.data == data):
            prev.next = None
                      
    def print_ll(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data)
            temp = temp.next
        print(temp.data)

obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_specific (25, 20)
obj.insert_at_begning(5)
obj.delete_element(30)
obj.print_ll()