class Solution(object):
    def reverseString(self, nums):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n= len(nums)
        for i in range (n//2):
            nums[i],nums[n-i-1]= nums[n-i-1],nums[i]
            

# nums.reverse()
