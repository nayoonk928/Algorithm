import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		double w = Double.parseDouble(st.nextToken());
		double r = Double.parseDouble(st.nextToken());
		
		double answer = w * (1 + r / 30);
		System.out.println((int)answer);
	}
}