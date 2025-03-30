package trees.binarySearchTree;

public class BinarySearchTree {
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

  public boolean lookup(int value) {
    Node temp = root;
    while (temp != null) {
      if (temp.value == value)
        return true;
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
    while (temp != null) {
      if (temp.value == oldValue) {
        temp.value = newValue;
        return true;
      }
      temp = oldValue < temp.value ? temp.left : temp.right;
    }
    return false;
  }

  // using recursion

  public boolean rContains(int value) {
    return rContains(root, value);
  }

  private boolean rContains(Node currentNode, int value) {
    if (currentNode == null)
      return false;
    if (currentNode.value == value)
      return true;

    if (value < currentNode.value) {
      return rContains(currentNode.left, value);
    } else {
      return rContains(currentNode.right, value);
    }
  }

  public void rInsert(int value) {
     root = rInsert(root, value);
  }

  private Node rInsert(Node currentNode, int value) {
    if (currentNode == null)
      return new Node(value);

    if (value < currentNode.value) {
      currentNode.left = rInsert(currentNode.left, value);
    } else if (value > currentNode.value) {
      currentNode.right = rInsert(currentNode.right, value);
    }
    return currentNode;
  }

  public void delete(int value) {
    root = deleteNode(root, value);
  }

  private Node deleteNode(Node currNode, int value) {
    if (currNode == null)
      return null;

    if (value < currNode.value) {
      currNode.left = deleteNode(currNode.left, value);
    } else if (value > currNode.value) {
      currNode.right = deleteNode(currNode.right, value);
    } else {
      if (currNode.left == null && currNode.right == null) {
        return null;
      } else if (currNode.left == null) {
        currNode = currNode.right;
      } else if (currNode.right == null) {
        currNode = currNode.left;
      } else {
        int subTreeMin = minValue(currNode.right);
        currNode.value = subTreeMin;
        currNode.right = deleteNode(currNode.right, subTreeMin);
      }
    }
    return currNode;
  }

  public int minValue(Node curNode) {
    while (curNode.left != null) {
      curNode = curNode.left;
    }
    return curNode.value;
  }

}