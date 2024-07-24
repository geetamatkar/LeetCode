class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal=max(candies)
        result=[]
        for i in range(len(candies)):
            sum = (candies[i]+extraCandies)
            if  (sum >= maxVal):
                result.append(bool(True))
            else:
                result.append(bool(False))
        return result
        