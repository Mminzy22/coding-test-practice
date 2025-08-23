class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sum=0;
        int size=0;
        for(int number: numbers){
            sum += number;
            size +=1;
        }
        System.out.println(sum); // 55
        System.out.println(size); // 10
        answer = (double)sum/size;
        return answer;
    }
}