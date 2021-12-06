# 1773. Count Items Matching a Rule

""" 
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        
        for i in items:

            if ruleKey == "type":
                if ruleValue== i[0]:
                    count +=1
            elif ruleKey == "color":
                if ruleValue == i[1]:
                    count +=1
            elif ruleKey == "name":
                if ruleValue == i[2]:
                    count +=1
            else:
                continue

        return count