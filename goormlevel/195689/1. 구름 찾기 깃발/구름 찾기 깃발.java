import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
	private static boolean valid(int x, int y, int n) {
		return x < n && x >= 0 && y < n && y >= 0;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int[][] directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
		int answer = 0;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				int cloud = 0;
				
				if (board[i][j] == 1) {
					continue;
				}
				
				for (int[] d : directions) {
					int nx = i + d[0];
					int ny = j + d[1];
					
					if (valid(nx, ny, n) && board[nx][ny] == 1) {
						cloud++;
					}
				}
				
				if (cloud == k) {
					answer++;
				}
			}
		}
		
		System.out.println(answer);
	}
}