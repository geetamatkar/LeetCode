class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        int [] out = new int[nums.length];
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(i%2 == 0){
                out[i] = nums[j];
                j++;
            }
            else{
                out[i] = nums[n];
                n++;
            }
        }
        
        return out;
        
    }
}