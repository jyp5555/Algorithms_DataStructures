import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] answer = {};
        for (int num : numlist){
            if (num % n == 0){
                int[] newarr = Arrays.copyOf(answer, answer.length+1);
                newarr[answer.length] = num;
                answer = newarr;
            }
        }
        return answer;
    }
}