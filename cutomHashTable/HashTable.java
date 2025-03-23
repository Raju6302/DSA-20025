package hashTable;

import java.util.ArrayList;

public class HashTable {
  private int size = 7;
  private Node[] datamap;

  class Node {
    String key;
    int value;
    Node next;

    public Node(String key, int value) {
      this.key = key;
      this.value = value;
    }
  }

  public HashTable() {
    datamap = new Node[size];
  }

  public int hash(String key) {
    int hash = 0;
    char[] keyChars = key.toCharArray();
    for (int i = 0; i < keyChars.length; i++) {
      int asciValue = keyChars[i];
      hash = (hash + asciValue * 23) % datamap.length;
    }
    return hash;
  }

  public void set(String key, int value) {
    int index = hash(key);
    Node newNode = new Node(key, value);
    if (datamap[index] == null) {
      datamap[index] = newNode;
    } else {
      Node temp = datamap[index];
      while (temp.next != null) {
        temp = temp.next;
      }
      temp.next = newNode;
    }
  }

  public int get(String key) {
    int index = hash(key);
    Node temp = datamap[index];
    while (temp != null) {
      if (temp.key.equals(key))
        return temp.value;
      temp = temp.next;
    }
    // if not found
    return -1;
  }

  public ArrayList<String> keys() {
    ArrayList<String> allKeys = new ArrayList<>();
    for (int i = 0; i < datamap.length; i++) {
      Node temp = datamap[i];
      while (temp != null) {
        allKeys.add(temp.key);
        temp = temp.next;
      }
    }
    return allKeys;
  }

  public ArrayList<Integer> values() {
    ArrayList<Integer> allKeys = new ArrayList<>();
    for (int i = 0; i < datamap.length; i++) {
      Node temp = datamap[i];
      while (temp != null) {
        allKeys.add(temp.value);
        temp = temp.next;
      }
    }
    return allKeys;
  }

  public void printHashTable() {
    for (int i = 0; i < datamap.length; i++) {
      System.out.println(i + ":");
      Node temp = datamap[i];
      while (temp != null) {
        System.out.println(" {" + temp.key + "= " + temp.value + "}");
        temp = temp.next;
      }
    }
  }
}
