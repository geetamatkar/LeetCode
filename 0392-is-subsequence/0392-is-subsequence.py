class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        itr = iter(t)
        return all(char in itr for char in s)

        
        