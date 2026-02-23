class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# Singly Linked List
class Singly_linked_list:
    def __init__(self, head = None):
        self.head = head

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        temp = self.head
        while(temp.data != position):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_node(self, data): # Doubt here
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
        if(temp.data == None):
            prev.next = None
        
    def print_ll(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data)
            temp = temp.next
        print(temp.data)
        

obj = Singly_linked_list()
obj.insert_at_begining(10)
obj.insert_at_begining(5)
obj.insert_at_end(15)
obj.insert_at_position(12, 10)
obj.delete_node(12)
obj.print_ll()
