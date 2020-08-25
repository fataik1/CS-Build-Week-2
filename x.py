
# For Duplicate problem

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) using a set to store the element
        # want to use set
        # if the element is not present.... insert element
        # else print the element 
        #if len(nums) is = len of set nums
        # return false
        #otherwise
        #return true
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        
        #another way
        """
        Can return the length of nums 
        Use counter to return any dups
        When using counter, it stores values & keys
                
        """
        # return len(nums) != len(Counter(nums).keys())
        
        