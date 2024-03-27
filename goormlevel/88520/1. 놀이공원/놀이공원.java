import java.io.*;
import java.lang.*;
import java.util.*;


public class Main {
	public static final Scanner scanner = new Scanner(System.in);
	
	public static void testCase(int caseIndex) {
		int N = scanner.nextInt();  // 지도의 크기 
		int K = scanner.nextInt();  // 놀이공원의 크기
		
		int[][] wastes = new int[N][N]; // 각 칸의 쓰레기 존재 여부 
		for (int r = 0; r < N; r += 1) {
			for (int c = 0; c < N; c += 1) {
				wastes[r][c] = scanner.nextInt();
			}
		}
		
		int answer = Integer.MAX_VALUE;
        
    // 모든 가능한 KxK 영역에 대해 순회
    for (int r = 0; r <= N - K; r++) {
      for (int c = 0; c <= N - K; c++) {
        // 현재 KxK 영역 내의 쓰레기 개수 계산
        int waste = 0;
        for (int i = r; i < r + K; i++) {
          for (int j = c; j < c + K; j++) {
            if (wastes[i][j] == 1) {
              waste++;
            }
        	}
        }
      	// 최소 쓰레기 개수 갱신
      	answer = Math.min(answer, waste);
    	}
    }
		
		System.out.println(answer);
	}
	
	public static void main(String[] args) throws Exception {
		int caseSize = scanner.nextInt();
		
		for (int caseIndex = 1; caseIndex <= caseSize; caseIndex += 1) {
			testCase(caseIndex);
		}
		
	}
	
}