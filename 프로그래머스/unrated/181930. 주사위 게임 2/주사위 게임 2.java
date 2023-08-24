class Solution {
    public int solution(int a, int b, int c) {
        int squareSum = a * a + b * b + c * c;
        int cubeSum = a * a * a + b * b * b + c * c * c;
        
        if (a == b && b == c && c == a) {
            return (a + b + c) * squareSum * cubeSum;
        } else if (a != b && b != c && c != a) {
            return a + b + c;
        } else {
            return (a + b + c) * squareSum;
        }
    }
}