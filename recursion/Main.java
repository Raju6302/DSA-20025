package recursion;

public class Main {
    public static void main(String[] args) {
        int res = factorial(5);
        System.out.println("Factorial of 5: " + res);

        System.out.println("Fibonacci(5): " + fibonacci(8));

        System.out.println("Sum of first 5 numbers: " + sumOfNumbers(5));

        System.out.println("Reversed string: " + reverseString("hello"));
    }

    public static int factorial(int n) {
        if (n == 1)
            return 1;
        return n * factorial(n - 1);
    }

     public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static int sumOfNumbers(int n) {
        if (n == 0) return 0;
        return n + sumOfNumbers(n - 1);
    }

    public static String reverseString(String str) {
        if (str.isEmpty()) return str;
        return reverseString(str.substring(1)) + str.charAt(0);
    }
}
