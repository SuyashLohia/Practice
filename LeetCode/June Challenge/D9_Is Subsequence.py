class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k=0
        n= len(s)
        for i in t:
            if k>=n:
                break
            if(i==s[k]):
                k+=1
                
        return k>=n
            