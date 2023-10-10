class Solution {
    public int solution(int a, int b) {
        int multiply = 2 * a * b;
        String str = a + "" + b ;
        int sum = Integer.parseInt(str);
        
        return multiply > sum ? multiply : sum;
    }
}