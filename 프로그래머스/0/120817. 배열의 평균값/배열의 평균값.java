import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        answer = Arrays.stream(numbers).average().orElse(0.0);
        return answer;
    }
}