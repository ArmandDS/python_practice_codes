#1672. Richest Customer Wealth

""" 
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_m = 0
        #iterate over each row, sum the columns and compare to the max, if greater then change the max, (order n)
        for i in range(len(accounts)):
            if sum(accounts[i])> max_m:
                max_m = sum(accounts[i])
                
        
        return max_m