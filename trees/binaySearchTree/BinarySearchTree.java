package trees.binaySearchTree;

public class BinarySearchTree {
    Node root;

  class Node{
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
      if (newNode.value == temp.value) return false; 
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

  public boolean lookup(int value) {
    Node temp = root;
    while (temp != null) {
      if (temp.value == value) return true;
      if (value < temp.value) {
        temp = temp.left;
      } else {
        temp = temp.right;
      }
    }
    return false;
  }

  public boolean update(int oldValue, int newValue) {
    Node temp = root;
    while ( temp != null) {
      if (temp.value == oldValue) {
        temp.value = newValue;
        return true;
      }
      temp = oldValue < temp.value ? temp.left : temp.right;
    }
    return false;
  }


}