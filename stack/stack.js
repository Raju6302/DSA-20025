class Node{
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class Stack{
    constructor(){
        this.top = null;
        this.length=0;
    }

    push(value){
        const node = new Node(value)
        if(top==null){
            top=node
            return
        }
        node.next = this.top
        this.top = node
        this.length++
    }
    pop(){
        if(this.top==null) return null
        const temp = this.top;
        this.top = this.top.next
        return temp
    }
    peek(){
        return this.top;
    }
    printStack(){
        if(this.top == null) return null
        let temp = this.top
        let output=""
        while(temp!=null){
            output+=temp.value + " -> "
            temp = temp.next;
        }
        console.log(output.slice(0,-4))
    }
}