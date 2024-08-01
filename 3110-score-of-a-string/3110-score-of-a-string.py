class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range (len(s)-1):
            ascii_value1 = ord(s[i])
            ascii_value2 = ord(s[i + 1])
            sum += abs( ascii_value1 - ascii_value2 )
            #print(sum)
            
        return sum
            
        