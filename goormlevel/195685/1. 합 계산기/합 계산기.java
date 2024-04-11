import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		int answer = 0;
		for (int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
		
			int num1 = Integer.parseInt(st.nextToken());
			String sign = st.nextToken();
			int num2 = Integer.parseInt(st.nextToken());
			
			if (sign.equals("+")) {
				answer += num1 + num2;
			} else if (sign.equals("-")) {
				answer += num1 - num2;
			} else if (sign.equals("/")) {
				answer += num1 / num2;
			} else if (sign.equals("*")) {
				answer += num1 * num2;
			}
		}
	
		System.out.print(answer);
	}
}