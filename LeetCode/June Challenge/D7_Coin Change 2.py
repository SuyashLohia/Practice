class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        comb=[1]
        comb+=[0]*amount
        for i in coins:
            for j in range(1,amount+1):
                if j>=i:
                    comb[j]+=comb[j-i]
                    
        return comb[amount]
                
  """
  Dynamic Programming Question, Solved using memoization

  """
