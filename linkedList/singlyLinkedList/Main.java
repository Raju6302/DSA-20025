package linkedList.singlyLinkedList;

public class Main {
  public static void main(String[] args) {
    LinkedList myLinkedList = new LinkedList(1);

    myLinkedList.append(2);
    myLinkedList.append(3);
    myLinkedList.append(4);
    myLinkedList.append(5);
    myLinkedList.append(6);
    myLinkedList.prepend(100);

    System.out.println("removed first element: " + " " + myLinkedList.removeFirst().value);
    System.out.println("removed last element: " + " " + myLinkedList.removeLast().value);

    myLinkedList.set(99, 0);
    myLinkedList.insert(100, 4);
    myLinkedList.remove(4);
    myLinkedList.remove(0);

    myLinkedList.reverse();


    myLinkedList.getHead();
    myLinkedList.getTail();
    myLinkedList.getLength();


    myLinkedList.printLinkedList();

    System.out.println("Lookup index element: " + " " + myLinkedList.get(3).value);
  }
}
