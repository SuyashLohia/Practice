class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        maxi=0
        i=0
        j=len(nums)-1
        while(i!=j):
            if(nums[i]>nums[j]):
                area=nums[j]*(j-i)
                j-=1
            else:
                area=nums[i]*(j-i)
                i+=1
            if(area>maxi):
                maxi=area              
        return maxi