package trees.traversals.breadthFirstSearch;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;


public class Bfs {
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

  // bfs row by row

  public ArrayList<Integer> BFS() {
    Node currentNode = root;
    Queue<Node> queue = new LinkedList<>();
    ArrayList<Integer> results = new ArrayList<>();

    if (currentNode == null) return results;

    queue.add(currentNode);

    while (queue.size() > 0) {
      currentNode = queue.remove();
      results.add(currentNode.value);
      if (currentNode.left != null) {
        queue.add(currentNode.left);
      }
      if (currentNode.right != null) {
        queue.add(currentNode.right);
      }
    }

    return results;
  }


  public static void main(String[] args) {
    Bfs myBfs = new Bfs();

    myBfs.insert(47);
    myBfs.insert(21);
    myBfs.insert(76);
    myBfs.insert(18);
    myBfs.insert(27);
    myBfs.insert(52);
    myBfs.insert(82);

      System.out.println( myBfs.BFS() );

    

  }
}