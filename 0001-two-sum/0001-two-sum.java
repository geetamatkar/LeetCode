class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Arrays.sort(nums);
        int a=0,b=0;
        int i=0,j,flag=0;
        while(i<nums.length)
        {
            for(j=(i+1);j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target){
                    flag = 1;
                    break;
                }
            }
            if(flag==1){
                a=i;
                b=j;
            break;
            }
            i++;
        }

        int [] arr = {a,b};
        return arr;
    }
}
        


  
    
