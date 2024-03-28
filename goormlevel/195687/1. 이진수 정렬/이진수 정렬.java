import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		Integer[] nums = new Integer[n];
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(nums, new Comparator<Integer>() {
			public int compare(Integer a, Integer b) {
				int countA = Integer.bitCount(a);
				int countB = Integer.bitCount(b);
				if (countA == countB) {
					return b - a;
				}
				return countB - countA;
			}
		});
		
		System.out.println(nums[k - 1]);
	}
}