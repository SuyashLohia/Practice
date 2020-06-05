class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range (len(nums)-2):
            if(nums[i]>0):
                break
            if (i>0 and nums[i]==nums[i-1]):
                continue
            lp,rp= i+1, len(nums)-1
            while(lp<rp):
                total = nums[i]+nums[lp]+nums[rp]
                
                if total<0:
                    lp+=1
                elif total>0:
                    rp-=1
                else:
                    result.append([nums[i],nums[lp],nums[rp]])
                    while (lp<rp and nums[lp]==nums[lp+1]):
                        lp+=1
                    while(lp<rp and nums[rp]==nums[rp-1]):
                        rp-=1
                    lp+=1
                    rp-=1
        return result
                    