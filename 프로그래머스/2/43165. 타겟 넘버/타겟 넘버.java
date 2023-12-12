class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }

    private int dfs(int[] numbers, int target, int index, int sum) {
        // 배열의 끝에 도달했을 때, 현재까지의 합이 타겟과 일치하는지 확인
        if (index == numbers.length) {
            return (sum == target) ? 1 : 0;
        }

        // 현재 숫자를 더하는 경우와 빼는 경우를 각각 재귀적으로 호출
        int add = dfs(numbers, target, index + 1, sum + numbers[index]);
        int subtract = dfs(numbers, target, index + 1, sum - numbers[index]);

        return add + subtract;
    }
}
