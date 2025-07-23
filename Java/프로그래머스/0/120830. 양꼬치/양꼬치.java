class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        answer = (n*12000)+(k*2000);
        for(int i=10; i<=n; i+=10){
            answer -= 2000;
        }
        return answer;
    }
}