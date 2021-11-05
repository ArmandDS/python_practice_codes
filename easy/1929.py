# leetcode 1929. Concatenation of Array

""" 
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        #Just extends the original array
        nums.extend(nums)
        return nums