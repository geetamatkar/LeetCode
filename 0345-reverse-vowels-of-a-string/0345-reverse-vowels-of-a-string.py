class Solution:
    def reverseVowels(self, s: str) -> str:
        result=list(s)
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left=0 
        right=len(s)-1
        
        while left<right:
            while left<right and result[left] not in vowels:
                left+=1
            while left<right and result[right] not in vowels:
                right-=1
            if left<right:
                result[left],result[right]=result[right],result[left]
                left+=1
                right-=1
                
        return ''.join(result)
        
        
            
        