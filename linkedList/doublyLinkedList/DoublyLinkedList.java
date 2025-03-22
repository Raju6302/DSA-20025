package linkedList.doublyLinkedList;

public class DoublyLinkedList {

  private Node head;
  private Node tail;
  private int length;

  class Node {
    int value;
    Node next;
    Node prev;

    public Node(int value) {
      this.value = value;
    }

  }

  public DoublyLinkedList(int value) {
    Node newNode = new Node(value);
    head = newNode;
    tail = newNode;
    length = 1;
  }

  public void append(int value) {
    Node newNode = new Node(value);
    if (head == null) {
      head = newNode;
      tail = newNode;
    } else {
      tail.next = newNode;
      newNode.prev = tail;
      tail = newNode;
    }
    length++;
  }

  public Node removeLast() {
    if (head == null)
      return null;

    Node temp = tail;

    if (head == tail) {
      head = null;
      tail = null;
    } else {
      tail = tail.prev;
      tail.next = null;
      temp.prev = null;
    }

    length--;
    return temp;
  }

  public void prepend(int value) {
    Node newNode = new Node(value);
    if (head == null) {
      head = newNode;
      tail = newNode;
    } else {
      newNode.next = head;
      head = newNode;
    }

    length++;

  }

  public Node removeFirst() {
    if (head == null) return null;
    Node temp = head;
    head = head.next;
    if (head != null) {
      head.prev = null;
    } else {
      tail = null;
    }
    temp.next = null;
    length--;
    return temp;

  }

  public Node get(int index) {
    if (index < 0 || index >= length) {
      return null;
    }
    Node temp = head;
    for (int i = 0; i < index; i++) {
      temp = temp.next;
    }

    return temp;
  }

  public boolean set(int value, int index) {
    Node temp = get(index);
    if (temp != null) {
      temp.value = value;
      return true;
    }

    return false;
  }

  public boolean insert(int value, int index) {
    if (index < 0 || index > length) return false;

    if (index == 0) {
      prepend(value);
      return true;
    }

    if (index == length) {
      append(value);
      return true;
    }

    Node newNode = new Node(value);
    Node before = get(index -1);
    Node after = before.next;
    before.next = newNode;
    newNode.next = after;
    after.prev = newNode;
    newNode.prev = before;
    length++;

    return true;

  }

  public Node remove(int index) {
    if (index < 0 || index >= length) return null;
    if (index == 0) return removeFirst();
    if (index == length -1) return removeLast();

    Node before = get(index -1);
    Node temp = before.next;
    Node after = temp.next;

    before.next = after;
    after.prev = before;
    temp.next = null;
    temp.prev = null;
    length--;

    return temp;

  }

  public void getHead() {
    System.out.println("head -> " + " " + head.value);
  }

  public void getTail() {
    System.out.println("Tail -> " + " " + tail.value);
  }

  public void getLength() {
    System.out.println("Length -> " + " " + length);
  }

  public void printDoublyLinkedList() {
    Node temp = head;
    while (temp != null) {
      System.out.println(temp.value);
      temp = temp.next;
    }
  }
}
