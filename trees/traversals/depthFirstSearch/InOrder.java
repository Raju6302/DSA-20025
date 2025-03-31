package trees.traversals.depthFirstSearch;

import java.util.ArrayList;

public class InOrder {
    Node root;

  class Node {
    int value;
    Node left;
    Node right;

    public Node(int value) {
      this.value = value;
    }
  }

  public boolean insert(int value) {
    Node newNode = new Node(value);
    if (root == null) {
      root = newNode;
      return true;
    }

    Node temp = root;

    while (true) {
      if (newNode.value == temp.value)
        return false;
      if (newNode.value < temp.value) {
        if (temp.left == null) {
          temp.left = newNode;
          return true;
        }
        temp = temp.left;
      } else {
        if (temp.right == null) {
          temp.right = newNode;
          return true;
        }
        temp = temp.right;
      }
    }
  }

  
  public ArrayList<Integer> inOrder() {
    ArrayList<Integer> results = new ArrayList<>();

    class Traverse {

      Traverse(Node currentNode) {

        if (currentNode.left != null) {
          new Traverse(currentNode.left);
        }

        results.add(currentNode.value);

        if (currentNode.right != null) {
          new Traverse(currentNode.right);
        }

      }
      
    }
    new Traverse(root);
    return results;
  }


   public static void main(String[] args) {
    InOrder myInOrder = new InOrder();

    myInOrder.insert(47);
    myInOrder.insert(21);
    myInOrder.insert(76);
    myInOrder.insert(18);
    myInOrder.insert(27);
    myInOrder.insert(52);
    myInOrder.insert(82);

      System.out.println( myInOrder.inOrder() );

    

  }
}
