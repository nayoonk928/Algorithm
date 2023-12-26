import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean flag = true;
        int cur = 1;

        Stack<Integer> stack = new Stack<>();
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            while (cur <= num) {
                stack.push(cur);
                answer.add("+");
                cur++;
            }

            if (stack.peek() == num) {
                stack.pop();
                answer.add("-");
            } else {
                System.out.println("NO");
                flag = false;
                break;
            }
        }

        if (flag) {
            for (String str : answer) {
                System.out.println(str);
            }
        }
    }
}