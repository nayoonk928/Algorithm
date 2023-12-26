import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    queue.add(num);
                    break;
                case "pop":
                    int pop = queue.isEmpty() ? -1 : queue.pop();
                    System.out.println(pop);
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    int empty = queue.isEmpty() ? 1 : 0;
                    System.out.println(empty);
                    break;
                case "front":
                    int front = queue.isEmpty() ? -1 : queue.peek();
                    System.out.println(front);
                    break;
                case "back":
                    int back = queue.isEmpty() ? -1 : queue.peekLast();
                    System.out.println(back);
                    break;
            }
        }
    }
}