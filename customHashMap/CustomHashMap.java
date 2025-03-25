package customHashMap;

public class CustomHashMap {
  private int size = 7;
    private int count = 0; 
    private Node[] table;
    private final double LOAD_FACTOR = 0.7;

    class Node {
        String key;
        int value;
        Node next;

        public Node(String key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public CustomHashMap() {
        table = new Node[size];
    }

    private int hash(String key) {
        int hash = 0;
        for (char ch : key.toCharArray()) {
            hash = (hash * 31 + ch) % table.length; 
        }
        return hash;
    }

    public void put(String key, int value) {
        if ((double) count / size > LOAD_FACTOR) {
            resize();
        }
        int index = hash(key);
        Node newNode = new Node(key, value);
        if (table[index] == null) {
            table[index] = newNode;
        } else {
            Node temp = table[index];
            while (temp.next != null) {
                if (temp.key.equals(key)) { 
                    temp.value = value;
                    return;
                }
                temp = temp.next;
            }
            temp.next = newNode;
        }
        count++;
    }

    public int get(String key) {
        int index = hash(key);
        Node temp = table[index];
        while (temp != null) {
            if (temp.key.equals(key)) {
                return temp.value;
            }
            temp = temp.next;
        }
        return -1;
    }

    public void remove(String key) {
        int index = hash(key);
        Node temp = table[index];
        Node prev = null;

        while (temp != null) {
            if (temp.key.equals(key)) {
                if (prev == null) {
                    table[index] = temp.next;
                } else {
                    prev.next = temp.next;
                }
                count--;
                return;
            }
            prev = temp;
            temp = temp.next;
        }
    }

    private void resize() {
        size *= 2;
        Node[] oldTable = table;
        table = new Node[size];
        count = 0;

        for (Node head : oldTable) {
            Node temp = head;
            while (temp != null) {
                put(temp.key, temp.value);
                temp = temp.next;
            }
        }
    }

    public void printHashMap() {
        for (int i = 0; i < table.length; i++) {
            System.out.println(i + ": ");
            Node temp = table[i];
            while (temp != null) {
              System.out.println(" {" + temp.key + "= " + temp.value + "}");
              temp = temp.next;
            }
        }
    }
}
