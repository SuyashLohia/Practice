import random
class Solution(object):
    
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = w
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i] + self.prefixSum[i - 1]
        
        # self.nw=[]
        # for i,j in enumerate(w):           
        #         self.nw+=[i]*j

    def pickIndex(self):
        """
        :rtype: int
        """
        if len(self.prefixSum) == 0:
            return 0
        target = random.randint(1, self.prefixSum[-1])
        start, end = 0, len(self.prefixSum)
        while start + 1 < end:
            
            mid = (start + end)//2
            if self.prefixSum[mid] < target:
                start = mid
            elif self.prefixSum[mid] > target:
                end = mid
            else:
                return mid
        if self.prefixSum[start] >= target:
            return start
        else:
            return end
        
        #return random.choice(self.nw)
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()