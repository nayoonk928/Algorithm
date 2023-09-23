class Solution {
    public int solution(int[] array) {
        int count = 0;

        for (int i = 0; i < array.length; i++) {
            int temp = array[i];
            while (temp > 0) {
                int digit = temp % 10;
                if (digit == 7) {
                    count++;
                }
                temp /= 10;
            }
        }

        return count;
    }
}