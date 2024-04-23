import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
public class Main {

    static final int MOD = 1_000_000_007;

    // 팩토리얼 계산 메서드 (모듈러 연산 적용)
    private static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result = (int)(((long)result * i) % MOD); // 모듈러 연산 적용
        }
        return result;
    }

    // 역원 계산 메서드 (페르마의 소정리 활용)
    private static int modInverse(int a) {
        return power(a, MOD - 2); // MOD의 역원은 (MOD-2) 승으로 계산됨
    }

    // 거듭제곱 계산 메서드 (분할정복을 활용하여 로그 시간에 계산)
    private static int power(int x, int y) {
        if (y == 0)
            return 1;
        int p = power(x, y / 2) % MOD;
        p = (int)(((long)p * p) % MOD);
        return (y % 2 == 0) ? p : (int)(((long)x * p) % MOD);
    }

    // 이항 계수 계산 메서드 (모듈러 연산 적용)
    private static int calculateBinomialCoefficient(int n, int k) {
        int numerator = factorial(n);
        int denominator = (int)(((long)factorial(k) * factorial(n - k)) % MOD); // 모듈러 연산 적용
        return (int)(((long)numerator * modInverse(denominator)) % MOD); // 모듈러 연산 적용
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        System.out.println(calculateBinomialCoefficient(n, k));
    }
    
}
