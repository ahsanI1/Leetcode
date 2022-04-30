class Solution {
    public int lengthOfLongestSubstring(String s) {
        int a_pointer = 0;
        int b_pointer = 0;
        int max = 0;
        
        HashSet<Character> hashSet = new HashSet<>();
        
        while (b_pointer < s.length()){
            if(hashSet.contains(s.charAt(b_pointer))){
                hashSet.remove(s.charAt(a_pointer));
                a_pointer++;
            }
            else{
                hashSet.add(s.charAt(b_pointer));
                b_pointer++;
                max = Math.max(max, hashSet.size());
            }
        }
    return max;
    }
}
