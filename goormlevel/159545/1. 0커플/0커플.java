import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] score = new int[n];
		for (int i = 0; i < n; i++) {
			score[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(score);
		
		int answer = 0;
		for (int i = 0; i < n / 2; i++) {
			int negative = score[i];
			int positive = score[n - i - 1];
			
			if (negative + positive != 0) {
				answer += negative + positive;
			}
		}
		
		System.out.println(answer);
	}
}