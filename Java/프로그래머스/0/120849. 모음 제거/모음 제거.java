class Solution {
    public String solution(String my_string) {
        String vowels = "aeiou";
        StringBuilder answer = new StringBuilder();
        
        for (char ch : my_string.toCharArray()) {
            if (vowels.indexOf(ch) == -1) {
                answer.append(ch);
            }
        }
        
        return answer.toString();
    }
}