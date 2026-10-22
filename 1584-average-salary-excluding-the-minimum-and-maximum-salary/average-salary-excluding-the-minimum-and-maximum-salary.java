class Solution {
    public double average(int[] salary) {
        int max=Integer.MIN_VALUE;
        int min=Integer.MAX_VALUE;
        int sum=0;
        int len=salary.length-2;
        for(int num:salary){
            sum+=num;
            if(num>max) max=num;
            if(num<min) min=num;
        }
        sum=sum-min-max;
        return  (double) sum/len;

    }
}