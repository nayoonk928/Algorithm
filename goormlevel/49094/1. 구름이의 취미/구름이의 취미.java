import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long n = Long.parseLong(br.readLine());
		
		long sum = (n * (n + 1) / 2) % 1000000007; 
		long answer = (sum * sum) % 1000000007; 
		
		System.out.println(answer);
	}
}