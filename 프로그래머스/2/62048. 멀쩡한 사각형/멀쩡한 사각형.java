class Solution {
    public long solution(int w, int h) {
        long totalSquares = (long)w * (long)h;
        long gcd = gcd(w, h);
        long cutSquares = (w / gcd + h / gcd - 1) * gcd;
        return totalSquares - cutSquares;
    }
    
    // 최대공약수를 구하는 메소드
    public long gcd(long a, long b) {
        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
