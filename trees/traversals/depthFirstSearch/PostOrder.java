package trees.traversals.depthFirstSearch;

import java.util.ArrayList;

public class PostOrder {
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

  
  public ArrayList<Integer> postOrder() {
    ArrayList<Integer> results = new ArrayList<>();

    class Traverse {

      Traverse(Node currentNode) {

        if (currentNode.left != null) {
          new Traverse(currentNode.left);
        }

        if (currentNode.right != null) {
          new Traverse(currentNode.right);
        }

        results.add(currentNode.value);
      }
      
    }
    new Traverse(root);
    return results;
  }


   public static void main(String[] args) {
    PostOrder myPostOrder = new PostOrder();

    myPostOrder.insert(47);
    myPostOrder.insert(21);
    myPostOrder.insert(76);
    myPostOrder.insert(18);
    myPostOrder.insert(27);
    myPostOrder.insert(52);
    myPostOrder.insert(82);

      System.out.println( myPostOrder.postOrder() );

    

  }
}
