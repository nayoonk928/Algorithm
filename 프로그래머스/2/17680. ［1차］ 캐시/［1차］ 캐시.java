import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Queue<String> cache = new LinkedList<>();
        
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        
        for (int i = 0; i < cities.length; i++) {
            String currentCity = cities[i].toLowerCase();

            // cache에 있는 경우
            if (cache.contains(currentCity)) {
                answer++;
                cache.remove(currentCity);
                cache.offer(currentCity);
            } else { // 없는 경우
                answer += 5;
                if (cache.size() == cacheSize) {
                    cache.poll();
                } 
                cache.offer(currentCity);
            }
        }
        
        return answer;
    }
}