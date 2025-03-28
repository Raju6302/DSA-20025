class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
        this.length=0
    }

    append(value){
        const node1 = new Node(value)
        if(this.head == null){
            this.head = node1;
        }else{
            let temp = this.head;
            while(temp.next != null){
                temp =temp.next;
            }
            temp.next = node1;
        }
        this.length++;
    }

    prepend(value){
        const node1 = new Node(value);
        node1.next = this.head;
        this.head = node1;
        this.length++;
    }

    getIndex(index){
        if(index<0 || index>this.length) return null
        let temp = this.head;
        for(let i=0;i<index;i++){
            temp = temp.next;
        }
        return temp
    }

    insert(index,value){
        if(index == 0) {
            this.prepend(value)
            return
        }
        if(index == this.length) {
            this.append(value)
            return
        }
        
        const new_node=new Node(value)
        let temp = this.getIndex(index-1)
        new_node.next = temp.next;
        temp.next = new_node
        this.length++
    }
    deleteFirst(){
        if(this.head==null) return null;

        let temp = this.head;
        this.head = temp.next;
        temp.next = null;
        this.length--;
        return temp;
    }
    deleteLast(){
        if(this.head==null) return null;

        let temp = this.head;
        let temp1=this.head;
        while(temp!=null){
            temp = temp.next;
            temp1.next=temp;
        }
        temp1.next=null
        this.length--;
        return temp1;
    }
    deleteIndex(index){
        if(index==0) this.deleteFirst()
        if(index==this.length) this.deleteLast()
        
        let temp = this.getIndex(index-1)
        let temp1= this.getIndex(index)

        temp.next = temp1.next;

        return temp1;
    }
    traverse(){
        let temp=this.head;
        let output=""
        while(temp!=null){
            output += temp.value + " -> "
            temp=temp.next;
        }
        console.log(output.slice(0,-4))
    }
    search(value){
        let temp = this.head;
        let i=0;
        if(temp.value!=value){
            temp=temp.next;
            i++;
        }

        return i;
    }
        
}



let list = new LinkedList()
//append
list.append(1)

//insert
list.insert(1,2)
list.insert(2,3)

//Prepend
list.prepend(0)

//Traversing the linked list and console logging
list.traverse()

//searching
console.log(list.search(1))

//delete the first node
list.deleteFirst()

//delete at an index
list.deleteIndex(1)

list.traverse()

