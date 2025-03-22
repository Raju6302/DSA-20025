package linkedList.doublyLinkedList;

public class Main {
  public static void main(String[] args) {
    DoublyLinkedList myDLL = new DoublyLinkedList(2);

    myDLL.append(3);

    myDLL.prepend(1);

   System.out.println(myDLL.removeFirst().value);

    System.out.println(myDLL.removeLast().value);

   System.out.println(myDLL.get(2).value);

  System.out.println(myDLL.set(99, 3));

  myDLL.insert(100, 1);

  myDLL.remove(1);


    myDLL.getHead();
    myDLL.getTail();
    myDLL.getLength();

    myDLL.printDoublyLinkedList();
  }
}
