class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newl=[]
        s = ''.join(map(str, digits)) 
        s= str(int(s)+1)
        for i in (s):
            newl.append(int(i))
        return (newl)