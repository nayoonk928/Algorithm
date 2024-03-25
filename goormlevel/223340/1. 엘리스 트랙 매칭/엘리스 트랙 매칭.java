import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());

    String[] friends = new String[n];
    for (int i = 0; i < n; i++) {
        friends[i] = st.nextToken();
    }
		
		String apply = br.readLine();
		
		int answer = 0;
		for (String friend : friends) {
			if (friend.equals(apply)) {
				answer++;
			}
		}
		
		System.out.println(answer);
	}
}