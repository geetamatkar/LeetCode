class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for op in operations:
            if op in ['X++', '++X']:
                X += 1
            
            if op in ['X--' , '--X']:
                X -= 1

        return X

    
        