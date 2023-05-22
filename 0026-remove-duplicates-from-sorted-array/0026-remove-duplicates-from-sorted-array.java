class Solution {
    public int removeDuplicates(int[] nums) {
        int length = nums.length;
        if(length==0)
        return 0;
        int a=1;
        for(int i=0;i<length-1;i++){
            if(nums[i]<nums[i+1]){
                nums[a]=nums[i+1];
                a++;

            }
            
        }
        return a;
    }
}

