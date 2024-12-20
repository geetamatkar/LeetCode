class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else "#"
                
                if bracket_map[char] != top:
                    return False
            
            else:
                stack.append(char)
                
        
        return not stack