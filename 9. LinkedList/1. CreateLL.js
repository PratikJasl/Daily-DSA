class node{
    constructor(value){
        this.value = value,
        this.next = null
    }
}

class LinkedList{
    constructor(value){
        this.head = {
            value: value,
            next: null
        }

        this.tail = this.head;
        this.length = 1;
    }    

    append(value){
        const newNode = new node(value);
        this.tail.next = newNode;
        this.tail = newNode
        this.length ++;
    } 
    
    prepend(value){
        const newNode = new node(value);
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
    }

    print(){
        const array = [];
        let current = this.head;
        while(current != null){
            array.push(current.value);
            current = current.next;
        }
        console.log(array);
    }

    insert(index, value){
        if(index >= this.length){
            return this.append(value);
        }
        if(index === 0){
            return this.prepend(value);
        }

        let newNode = new node(value);
        let pointer = this.head;
        for(let i = 0; i < index-1; i++){
           pointer = pointer.next;
        }
        newNode.next = pointer.next;
        pointer.next = newNode;
        this.length++;
    }

    delete(index){
        if(index === 0){
            if(!this.head){
                return "List is Empty";
            }else{
                this.head = this.head.next;
            }
        }
        let pointer = this.head;
        for(let i = 0; i < index-1; i++){
            pointer = pointer.next;
        }
        let unwantedNode = pointer.next;
        pointer.next = unwantedNode.next;
        this.length--;
    }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 20);
myLinkedList.insert(0, 20);
myLinkedList.print();
myLinkedList.delete(0);
myLinkedList.print();

