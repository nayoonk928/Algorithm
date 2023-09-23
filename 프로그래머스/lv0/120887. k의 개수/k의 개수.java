class Solution {
    public int solution(int i, int j, int k) {
        int count = 0;

        for (int num = i; num <= j; num++) {
            int temp = num;
            while (temp > 0) {
                int digit = temp % 10;
                if (digit == k) {
                    count++;
                }
                temp /= 10;
            }
        }

        return count;
    }
}