import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();

        for (int i = 0; answer.length() < t * m; i++) {
            answer.append(convertToBase(i, n));
        }

        StringBuilder result = new StringBuilder();
        for (int i = p - 1; i < t * m; i += m) {
            result.append(answer.charAt(i));
        }

        return result.toString();
    }

    private String convertToBase(int number, int base) {
        StringBuilder result = new StringBuilder();
        
        if (number == 0) {
            return "0";
        }
        
        while (number > 0) {
            int remainder = number % base;
            char digit = (char) (remainder < 10 ? '0' + remainder : 'A' + remainder - 10);
            result.insert(0, digit);
            number /= base;
        }
        
        return result.toString();
    }
}
