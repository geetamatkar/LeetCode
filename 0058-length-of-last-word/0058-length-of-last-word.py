class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s.strip())
        result = s.strip().split(" ")
        print(result)
        
        lenVal = len(result[-1])
        
        return lenVal
        