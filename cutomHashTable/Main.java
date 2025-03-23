package hashTable;

public class Main {
  public static void main(String[] args) {
    HashTable myHashTable = new HashTable();
    
    myHashTable.set("raj", 100);
    myHashTable.set("bheem", 200);
    myHashTable.set("ram", 300);
    myHashTable.set("kai", 400);
    myHashTable.set("priya", 500);

    System.out.println(myHashTable.get("priya"));

    System.out.println(myHashTable.keys());
    System.out.println(myHashTable.values());

    myHashTable.printHashTable();

  }
}
