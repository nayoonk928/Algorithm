import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int pain = Integer.parseInt(br.readLine());
		int itemCount = 0;
		
		itemCount += pain / 14;
		pain %= 14;
		
		if (pain >= 7) {
			itemCount++;
			pain -= 7;
		}
		
		itemCount += pain;
		
		System.out.println(itemCount);
	}
}