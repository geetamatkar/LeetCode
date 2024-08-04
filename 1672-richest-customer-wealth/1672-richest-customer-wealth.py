class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        maxm = 0
        for i in range (len(accounts)):
            total = sum(accounts[i])
            maxm = max(maxm,total)
            
        return maxm
            
        