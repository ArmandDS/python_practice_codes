# 1528. Shuffle String

"""  
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        #create an emptu array 
        r = ['']*len(s)
        
        #iterate over a zip of the string and the indeces to shuffle
        for ch, i in zip(s, indices):
            #change the index to the correspond character
            r[i] = ch
        
        #return the string    
        return "".join(r)
        