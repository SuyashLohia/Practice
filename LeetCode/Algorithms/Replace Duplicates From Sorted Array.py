class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t= len(nums)
        k=None
        c=0
        for i in range(t):
            if nums[i-c]!=k:
                k=nums[i-c]
            else:
                nums.pop(i-c)
                c+=1
                
        return len(nums)

"""
Better Method 
newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

 """
