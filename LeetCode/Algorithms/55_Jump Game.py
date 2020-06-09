class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        lastPos = len(nums)-1
        for i in range (len(nums)-1,-1,-1):
            if (i + nums[i] >= lastPos):
                lastPos = i
            
        
        return lastPos == 0
    
"""
Best Approach: GREEDY ALGORITHM:

Alternate Approaches:

1) Backtracking (Recursion) : Basically going through every possible combiniation
    - Top Down Approach 
    - Botto Up Approach 
    
2) Dynamic Programming: Using Memoization to create an array which stores the status of the index( good,bad,unkown)
    - Top Down Approach 
    - Bottom Up Approach (Similar to greedy algorithm)

"""