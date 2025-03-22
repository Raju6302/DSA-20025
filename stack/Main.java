package stack;

public class Main {
  public static void main(String[] args) {
    Stack stack = new Stack(99);

    stack.push(400);
    stack.push(500);

    System.out.println("pop: " + " " +stack.pop().value);
    System.out.println("pop: " + " " +stack.pop().value);

    stack.getTop();
    stack.getLength();
    stack.printStack();

  }
}