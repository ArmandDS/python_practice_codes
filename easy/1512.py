# 1512. Number of Good Pairs

"""  
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hash1 = {}
        
        #first create and array with the count of the element presence
        for i in nums:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] +=1
                
        count = 0
        #then with the formula to compute the number of pairs in a list: N*(N-1)/2 we get the pairs
        for k,v in hash1.items():
            count += (v*(v-1))//2
            
        return count
            