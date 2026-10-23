class Solution {
    public char findTheDifference(String s, String t) {
        int result=0;
        for(int i=0;i<s.length();i++){
            result=result^s.charAt(i);
        }
        for(int j=0;j<t.length();j++){
            result=result^t.charAt(j);
        }
        return (char)result;
    }
}