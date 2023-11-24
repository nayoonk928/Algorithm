class Solution {
    public int solution(String my_string) {
        int sum = 0;
        StringBuilder currentNumber = new StringBuilder();

        for (char c : my_string.toCharArray()) {
            if (Character.isDigit(c)) {
                // 현재 문자가 숫자인 경우 현재 숫자를 만들어감
                currentNumber.append(c);
            } else {
                // 현재 문자가 숫자가 아닌 경우, 지금까지 만들어진 숫자를 더하고 초기화
                if (currentNumber.length() > 0) {
                    sum += Integer.parseInt(currentNumber.toString());
                    currentNumber = new StringBuilder();
                }
            }
        }

        // 마지막으로 만들어진 숫자를 더해줌
        if (currentNumber.length() > 0) {
            sum += Integer.parseInt(currentNumber.toString());
        }

        return sum;
    }
}