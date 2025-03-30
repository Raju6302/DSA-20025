package trees.binaySearchTree;

public class Main {
  public static void main(String[] args) {
    BinarySearchTree myBST = new BinarySearchTree();
    myBST.insert(37);
    myBST.insert(21);
    myBST.insert(76);
    myBST.insert(18);
    myBST.insert(52);
    myBST.insert(82);

    myBST.insert(27);

    System.out.println(myBST.update(27, 99));

    System.out.println(myBST.root.value);
    System.out.println(myBST.root.left.value);
    System.out.println(myBST.root.right.value);
    System.out.println(myBST.root.left.left.value);
    System.out.println(myBST.root.left.right.value);
    System.out.println(myBST.root.right.left.value);
    System.out.println(myBST.root.right.right.value);


    System.out.println(myBST.lookup(82));

   System.out.println(myBST.rContains(21));
  }
}
