package hashMap;

public class Main {
  public static void main(String[] args) {
    CustomHashMap myMap = new CustomHashMap();

    myMap.put("raj", 10);
    myMap.put("bheem", 200);
    myMap.put("ram", 300);
    myMap.put("kai", 400);
    myMap.put("priya", 500);

    System.out.println("Get 'kai': " + myMap.get("kai"));
    System.out.println("Get 'bheem': " + myMap.get("bheem"));

    myMap.printHashMap();

    myMap.remove("priya");

    System.out.println("After removing: ");
    myMap.printHashMap();
  }
}
