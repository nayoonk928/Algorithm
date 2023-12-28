import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "push_front":
                    int pushFront = Integer.parseInt(st.nextToken());
                    deque.addFirst(pushFront);
                    break;
                case "push_back":
                    int pushBack = Integer.parseInt(st.nextToken());
                    deque.addLast(pushBack);
                    break;
                case "pop_front":
                    int popFront = deque.isEmpty() ? -1 : deque.pollFirst();
                    System.out.println(popFront);
                    break;
                case "pop_back":
                    int popBack = deque.isEmpty() ? -1 : deque.pollLast();
                    System.out.println(popBack);
                    break;
                case "size":
                    System.out.println(deque.size());
                    break;
                case "empty":
                    int empty = deque.isEmpty() ? 1 : 0;
                    System.out.println(empty);
                    break;
                case "front":
                    int front = deque.isEmpty() ? -1 : deque.peekFirst();
                    System.out.println(front);
                    break;
                case "back":
                    int back = deque.isEmpty() ? -1 : deque.peekLast();
                    System.out.println(back);
                    break;
            }
        }
    }
}