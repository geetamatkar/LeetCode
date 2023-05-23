class Solution {
    public int[] getConcatenation(int[] nums) {
        int [] out = new int[nums.length*2];
        for(int i=0;i<out.length;i++){
            if(i<nums.length){
                out[i]=nums[i];
            }
            else{
                out[i] = nums[i-nums.length];
            }
        }
        
        return out;
        
    }
}