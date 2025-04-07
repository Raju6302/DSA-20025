class Node {
  constructor(value) {
    this.prev = null;
    this.next = null;
    this.value = value;
  }
}

class DLL {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  getLength(){
    return this.length;
  }
  append(value) {
    const node = new Node(value);
    if (this.head == null && this.tail== null) {
      this.head = this.tail = node;
      console.log(this.tail)
      this.length++;
      return;
    }
    
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = this.tail.next;
    this.length++;
  }
  prepend(value) {
    const node = new Node(value);
    if (this.head == null && this.tail == null) {
      this.head = this.tail = node;
      this.length++;
      return;
    }
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
    this.length++;
  }
  insert(index, value) {
    if (index < 0 && index > this.length) return;
    if (index == 0) {
      this.prepend(value);
      return;
    }
    if (index == this.length) {
      this.append(value);
      return;
    }
    const node = new Node(value);
    const temp = this.getIndex(index - 1);
    node.next = temp.next;
    node.prev = temp;
    temp.next.prev = node
    temp.next = node;
    this.length++
  }
  getIndex(index) {
    if (index > this.length) return null;

    let temp = this.head;
    for (let i = 0; i != index; i++) {
      temp = temp.next;
    }
    return temp;
  }
  removeFirst() {
    if (this.head == null) return null;
    if(this.head == this.tail){
        const temp = this.head;
        this.head = this.tail = null
        this.length--;
        return temp
    }

    const temp = this.head;
    this.head = this.head.next;
    this.head.prev = null;
    temp.next = null;
    this.length--;
    return temp;
  }
  removeLast() {
    if (this.head == null && this.tail==null) return null;
    if(this.head == this.tail){
        const temp = this.head;
        this.head = this.tail = null
        this.length--;
        return temp
    }
    const temp = this.tail;
    this.tail = this.tail.prev;
    this.tail.next = null;
    temp.prev = null;
    this.length--;
    return temp;
  }
removeIndex(index){
  if(this.head == null) return null
  if (index == 0) return this.removeFirst()
  if(index == this.length-1) return this.removeLast()

  const temp = this.getIndex(index)
  const Prev = temp.prev;
  const Next = temp.next;
  Prev.next = Next
  Next.prev = Prev

  temp.prev=null
  temp.next = null

  this.length--

  return temp
}

traverseList(){
    let temp = this.head
    let output = ""
    while(temp!=null){
        output += temp.value + "->"
        temp = temp.next;
    }
    console.log(output.slice(0,-2))
  }
  reverseTraverseList(){
    let temp = this.tail
    let output = "";
    while(temp!=null){
      output += temp.value + "->"
      temp = temp.prev
    }
    console.log(output.slice(0,-2))
  }
}

const dll = new DLL()

dll.append(2)
dll.prepend(0)
dll.insert(1,1)
dll.append(3)
dll.append(4)
console.log("Length: " + dll.getLength())
dll.traverseList()
dll.reverseTraverseList()
const rmF = dll.removeFirst()
const rmL = dll.removeLast()
dll.traverseList()
const temp = dll.getIndex(1)
console.log(temp.value)
const rmI = dll.removeIndex(1);
dll.traverseList()


