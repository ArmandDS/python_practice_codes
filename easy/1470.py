# 1470. Shuffle the Array

""" 
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        r = []
        #iterate over a zip with two list, the fist is the first half of the original list and the second is the second half of the original list
        for x,y in zip(nums[:n], nums[n:]):
            r.append(x)
            r.append(y)
                   
        return r
        