class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            newt = target - i
            nnums=nums.copy()
            nnums.pop(nums.index(i))
            if(newt in nnums):
                t= nums.index(i)
                return [t,nums.index(newt,t+1)]