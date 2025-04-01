package trees.traversals.depthFirstSearch;

import java.util.ArrayList;


public class PreOrder {
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

  // PreOrder go left as long as possible until currentNode.left is not equal to null and do the same for right as well.

  public ArrayList<Integer> preOrder() {
    ArrayList<Integer> results = new ArrayList<>();

    class Traverse {

      Traverse(Node currentNode) {

        results.add(currentNode.value);

        if (currentNode.left != null) {
          new Traverse(currentNode.left);
        }

        if (currentNode.right != null) {
          new Traverse(currentNode.right);
        }
      }
      
    }
    new Traverse(root);
    return results;
  }


   public static void main(String[] args) {
    PreOrder myPreOrder = new PreOrder();

    myPreOrder.insert(47);
    myPreOrder.insert(21);
    myPreOrder.insert(76);
    myPreOrder.insert(18);
    myPreOrder.insert(27);
    myPreOrder.insert(52);
    myPreOrder.insert(82);

      System.out.println( myPreOrder.preOrder() );

    

  }
}
