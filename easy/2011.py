#2011. Final Value of Variable After Performing Operations

""" 
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        #iterate and find the operation, then apply it
        for op in operations:
            
            if op == "X++" or op == "++X":
                x +=1
            
            else:
                x -=1
                
        
        return x