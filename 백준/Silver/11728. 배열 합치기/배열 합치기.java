import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();

        int[] A = new int[n];
        int[] B = new int[m];

        for (int i = 0; i < n; i++) {
            A[i] = scanner.nextInt();
        }

        for (int i = 0; i < m; i++) {
            B[i] = scanner.nextInt();
        }

        int[] result = new int[A.length + B.length];
        int a = 0, b = 0, r = 0;

        while (a < A.length || b < B.length) {
            if (b >= B.length || (a < A.length && A[a] <= B[b])) {
                result[r++] = A[a++];
            } else {
                result[r++] = B[b++];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : result) {
            sb.append(num+" ");
        }
        System.out.println(sb);
    }
}