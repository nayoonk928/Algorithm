class Solution {
    public int[] solution(int[] arr) {
        // 주어진 배열의 길이를 저장
        int length = arr.length;

        // 2의 거듭제곱인지 확인
        while ((length & (length - 1)) != 0) {
            // 2의 거듭제곱이 아니라면 배열의 뒤에 0 추가
            length++;
        }

        // 결과 배열 생성 및 값 복사
        int[] answer = new int[length];
        System.arraycopy(arr, 0, answer, 0, arr.length);

        return answer;
    }
}