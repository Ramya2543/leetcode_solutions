class Solution {
    public boolean check(int[] nums) {
        int count=0;
        int n=nums.length;
        for(int i=0;i<n-1;i++){
            //checking if current element is greater than nextelement we notice 
            //one drop so we increment the count
            if(nums[i]>nums[i+1]){
                count++;
            }
        }
        //we aslo check the last element with first element because we assume 
        //array as circular
            if(nums[n-1]>nums[0]){
                count++;
            }
            //for valid rotated and sorted array breakpoints at most 1 
            //i.e the count must be 0 and 1 only if greater than 1 invalid
            if(count>1){
                return false;
            }
        return true;
    }
}