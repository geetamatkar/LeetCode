class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for num in nums:
            if (num % 3 != 0):
                if((num-1) % 3 == 0) or ((num+1) % 3 == 0):
                    cnt+=1
                    
        return cnt
                
                
            
        