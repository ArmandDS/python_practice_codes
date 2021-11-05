#1365. How Many Numbers Are Smaller Than the Current Number

"""  
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        #create a ordered list
        sortedNums = sorted(nums)
        hmap = {}
        ans = []
        #Fill a dictionay with the element as key and the index as value        
        for i in range(len(sortedNums)):
            if sortedNums[i] not in hmap:
                hmap[sortedNums[i]] = i
        #iterate over the unordered list and append to a new list the value if that element in the dictionay which is how many element are smaller
        for i in nums:
            ans.append(hmap[i])
		
        return ans