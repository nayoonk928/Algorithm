class Solution {
    public int solution(int order) {
        int answer = 0;
        String orderStr = String.valueOf(order);

        for (char digit : orderStr.toCharArray()) {
            if (digit == '3' || digit == '6' || digit == '9') {
                answer++;
            }
        }

        return answer;
    }
}
