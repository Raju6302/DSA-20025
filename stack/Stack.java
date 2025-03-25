package stack;

public class Stack {

  private Node top;
  private int length;

  class Node {
    int value;
    Node next;

    public Node(int value) {
      this.value = value;
    }
  }

  public Stack(int value) {
    Node newNode = new Node(value);
    top = newNode;
    length = 1;
  }

  public void push(int value) {
    Node newNode = new Node(value);
    if (top == null) {
      top = newNode;
    } else {
      newNode.next = top;
      top = newNode;
    }
    length++;
  }

  public Node pop() {
    if (top == null)
      return null;

    Node temp = top;
    top = top.next;
    temp.next = null;
    length--;

    return temp;
  }

  public void printStack() {
    Node temp = top;
    while (temp != null) {
      System.out.println(temp.value);
      temp = temp.next;
    }
  }

  public void getTop() {
    System.out.println("Top: " + " " + top.value);
  }

  public void getLength() {
    System.out.println("Length: " + " " + length);
  }
}