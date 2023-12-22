import java.util.*;

class Solution {
    public int solution(String numbers) {
        int answer = 0;
        String[] strings = numbers.split("");
        Set<String> combinations = generateCombinations(strings);

        for (String combination : combinations) {
            if (!combination.isEmpty() && isPrime(Integer.parseInt(combination))) {
                answer++;
            }
        }

        return answer;
    }

    private Set<String> generateCombinations(String[] strings) {
        Set<String> result = new HashSet<>();
        boolean[] visited = new boolean[strings.length];
        generateCombinationsHelper(strings, visited, "", result);
        return result;
    }

    private void generateCombinationsHelper(String[] strings, boolean[] visited, String current, Set<String> result) {
        // 현재 조합을 결과에 추가 (단, 비어있지 않은 경우에만 추가)
        if (!current.isEmpty()) {
            result.add(removeLeadingZeros(current));
        }

        // 현재 인덱스부터 끝까지 반복
        for (int i = 0; i < strings.length; i++) {
            // 해당 숫자가 이미 사용되었으면 건너뛰기
            if (visited[i]) {
                continue;
            }

            // 다음 문자열을 현재 조합에 추가
            visited[i] = true;
            generateCombinationsHelper(strings, visited, current + strings[i], result);
            visited[i] = false;
        }
    }
    
    private String removeLeadingZeros(String s) {
        return s.replaceFirst("^0+(?!$)", "");
    }

    private boolean isPrime(int number) {
        if (number < 2) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }
}
