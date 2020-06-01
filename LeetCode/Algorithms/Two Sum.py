class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            newt = target - i
            nnums=nums.copy()
            nnums.pop(nums.index(i))
            if(newt in nnums):
                t= nums.index(i)
                return [t,nums.index(newt,t+1)]

'''
Better Code:
if len(nums) <= 1:
    return False
buff_dict = {}
for i in range(len(nums)):
    if nums[i] in buff_dict:
        return [buff_dict[nums[i]], i]
    else:
        buff_dict[target - nums[i]] = i
'''