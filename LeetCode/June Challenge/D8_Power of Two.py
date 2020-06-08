class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        while(n==1 or n%2==0):
            if(n==1):
                return True
            else:
                n/=2
        return False
    
    
'''
Other Approaches:

1) return n > 0 && ((n & (n-1)) == 0);                               // Bit Manipulation
2) return n > 0 && (n == 1 || (n%2 == 0 && isPowerOfTwo(n/2)));      // Recursively