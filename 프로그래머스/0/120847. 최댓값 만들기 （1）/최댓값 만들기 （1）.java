class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        //Solution 1. 정렬 후 max, secondmax 구한 다음 곱한 값 리턴
        
        //Solution 2. numbers를 순회하면서 max 값 찾기
        int max=0;
        int secondMax=0;
        for (int i=0; i<numbers.length; i++){
            if (numbers[i] > max){
                secondMax = max;
                max = numbers[i];
            }
            else if (numbers[i] > secondMax){
                secondMax = numbers[i];
            }
        }
        answer = max*secondMax;
        return answer;
    }
}