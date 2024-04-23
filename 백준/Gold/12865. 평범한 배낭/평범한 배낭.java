import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] bags = new int[n][2];
        for (int i = 0; i < n; i++) {
            bags[i][0] = sc.nextInt();
            bags[i][1] = sc.nextInt();
        }

        System.out.println(getMaxValue(bags, n, k));
    }

    private static int getMaxValue(int[][] bags, int n, int k) {
        int[][] dp = new int[n + 1][k + 1];

        for (int i = 1; i <= n; i++) {
            int weight = bags[i - 1][0];
            int value = bags[i - 1][1];
            for (int j = 1; j <= k; j++) {
                if (weight > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight] + value);
                }
            }
        }

        return dp[n][k];
    }
}