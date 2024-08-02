class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        i= 0
        #for i in range (len(nums)):
        while i< len(nums):
            if nums[i] == 0:
                cnt+=1
                nums.pop(i)
            
            else:
                i+=1
            #i+=1
                
        for i in range (1, cnt+1):
            nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
        