class Node{
    constructor(value){
        this.value = value
        this.next= null
    }
}
class Queue{
    constructor(){
        this.first=null
        this.last=null
        this.length=0
    }

    createQueue(value){
        let node = new Node(value)
        this.first = node
        this.last = node
    }

    enQueue(value){
        const node = new Node(value)
        if(this.first==null) {
            this.first = node
            this.last = node
            return
        }
        this.last.next = node
        this.last = node
    }
    deQueue(){
        if (this.first == null) return null
        let temp = this.first
        if(this.first==this.last){
            this.first = this.last = null;
        } else {
            this.first = temp.next
            temp.next = null
        }
        return temp;
    }
    printQueue(){
        if(this.first == null) return null
        let temp = this.first
        let output=""
        while(temp!=null){
            output+=temp.value + " -> "
            temp = temp.next;
        }
        console.log(output.slice(0,-4))
    }
}

let q = new Queue();

q.createQueue(1)
q.enQueue(2)
q.enQueue(3)
console.log(q.deQueue().value)

q.printQueue()

