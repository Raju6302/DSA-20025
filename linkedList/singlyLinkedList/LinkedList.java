package linkedList.singlyLinkedList;

public class LinkedList {

  private Node head;
  private Node tail;
  private int length;

  class Node {
    int value;
    Node next;

    public Node(int value) {
      this.value = value;
    }

  }

  public LinkedList(int value) {
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
      tail = newNode;
    }
    length++;
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

    if (head == null) {
      return null;
    }

    Node temp = head;
    head = head.next;
    if (head == null) {
      tail = null;
    }
    temp.next = null;
    length--;
    return temp;
  }

  public Node removeLast() {
    if (head == null) {
      return null;
    }

    Node temp = head;
    Node prev = head;

    while (temp.next != null) {
      prev = temp;
      temp = temp.next;
    }
    tail = prev;
    prev.next = null;
    length--;
    if (length == 0) {
      head = null;
      tail = null;
    }
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
    Node temp = get(index - 1);
    newNode.next = temp.next;
    temp.next = newNode;
    length++;

    return true;
    
  }

  public Node remove(int index) {
    if (index < 0 || index >= length) return null;
    if (index == 0) return removeFirst();
    if (index == length - 1) return removeLast();

    Node prev = get(index - 1);
    Node temp = prev.next;

    prev.next = temp.next;
    temp.next = null;
    length--;
    return temp;
  }

  public void reverse() {
    Node temp = head;
    head = tail;
    tail = temp;

    Node before = null;
    Node after = temp.next;

    for (int i = 0; i < length; i++) {
      after = temp.next;
      temp.next = before;
      before = temp;
      temp = after;
    }
  }

  public void printLinkedList() {
    Node temp = head;
    while (temp != null) {
      System.out.println(temp.value);
      temp = temp.next;
    }
  }

  public void getHead() {
    System.out.println("Head -> " + " " + head.value);
  }

  public void getTail() {
    System.out.println("Tail -> " + " " + tail.value);
  }

  public void getLength() {
    System.out.println("Length -> " + " " + length);
  }

}