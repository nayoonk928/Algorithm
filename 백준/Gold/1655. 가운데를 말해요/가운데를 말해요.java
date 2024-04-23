import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
public class Main {
    
    // 최대 힙과 최소 힙에 수를 삽입하는 메서드
    private static void addNumber(PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap, int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }
        
        balanceHeaps(maxHeap, minHeap);
    }

    // 최대 힙과 최소 힙의 크기를 맞추는 메서드
    private static void balanceHeaps(PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap) {
        while (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        }
        while (maxHeap.size() < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    // 중간값을 계산하는 메서드
    private static int calculateMedian(PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap) {
        if (maxHeap.size() == minHeap.size()) {
            return maxHeap.peek();
        } else {
            return maxHeap.peek();
        }
    }

    // 중간값을 계산하고 StringBuilder에 추가하는 메서드
    private static void printMedian(PriorityQueue<Integer> maxHeap, PriorityQueue<Integer> minHeap, int num, StringBuilder sb) {
        addNumber(maxHeap, minHeap, num);
        int median = calculateMedian(maxHeap, minHeap);
        sb.append(median).append("\n");
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            printMedian(maxHeap, minHeap, num, sb);
        }
        
        System.out.print(sb.toString());
    }
    
}
