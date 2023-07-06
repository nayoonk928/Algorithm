import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new LinkedList<>();
        int count = 0;

        // get N, M
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // get element's location
        int[] location = new int[m];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            location[i] = Integer.parseInt(st2.nextToken());
        }

        // create queue
        IntStream.range(1, n + 1).forEach(x -> deque.add(x));

        for (int target : location) {
            int index = 0;

            for (int x : deque) {
                if (x == target) { // get target's index
                    break;
                }
                index++;
            }

            if (index <= deque.size() - index) {
                while (deque.peekFirst() != target) {
                    deque.addLast(deque.pollFirst());
                    count++;
                }
            } else {
                while (deque.peekFirst() != target) {
                    deque.addFirst(deque.pollLast());
                    count++;
                }
            }
            deque.pollFirst();
        }
        System.out.println(count);
    }
}