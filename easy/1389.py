# 1389. Create Target Array in the Given Order

""" 
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
"""

# the deque collection include insert of O(1) and pop of O(1)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        result = []*len(nums)
        import collections
        
        c = collections.deque([])
        
        for i in range(len(nums)):
            c.insert(index[i],nums[i])
            
        
        result = list(c)
        
        return result