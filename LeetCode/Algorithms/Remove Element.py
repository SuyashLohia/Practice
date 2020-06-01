class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=0
        for i in range (len(nums)):
            if nums[i-c]==val:
                nums.pop(i-c)
                c+=1
                
        return len(nums)