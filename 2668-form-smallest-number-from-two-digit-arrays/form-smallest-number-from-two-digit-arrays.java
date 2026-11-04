class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
      HashSet<Integer>set=new HashSet<>();
      for(int i=0;i<nums1.length;i++){
        set.add(nums1[i]);
        }
        int common=10;
        for(int i=0;i<nums2.length;i++){
            if(set.contains(nums2[i])){
                common=Math.min(common,nums2[i]);
            }
        }
        if(common!=10){
            return common;
        }
        int min1=nums1[0];
        int min2=nums2[0];
        for(int i=0;i<nums1.length;i++){
            min1=Math.min(min1,nums1[i]);
        }
        for(int i=0;i<nums2.length;i++){
            min2=Math.min(min2,nums2[i]);
        }
        int num1=min1*10+min2;
        int num2=min2*10+min1;
        return Math.min(num1,num2);
    }
}