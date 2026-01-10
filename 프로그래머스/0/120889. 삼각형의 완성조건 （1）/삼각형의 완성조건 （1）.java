import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int answer = 2;
        int totalSum = Arrays.stream(sides).sum();
        int max = 0;
        for (int i=0; i<sides.length; i++){
            if (sides[i] > max){
                max = sides[i];
            }
        }
        
        if (totalSum-max > max){
            answer = 1;
        }
        return answer;
    }
}