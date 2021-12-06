# 2006. Count Number of Pairs With Absolute Difference K

""" 
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

"""


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        hmap = {}
        
        count = 0
        
        hmap[nums[0]] = 1
        for n in nums[1:]:
            
            if n+k in hmap:
                count += hmap[n+k]
            if  n-k in hmap:
                count += hmap[n-k]
                
            if n in hmap:
                hmap[n] +=1
            else:
                hmap[n] =1
        return (count)
            