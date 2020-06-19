class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix)==0 or len(matrix[0])==0):
            return False
        l,r=0,len(matrix)-1
        mid=0
        while l<=r:
            mid=(l+r)//2
            if target<matrix[mid][0]:
                r=mid-1
            elif target>matrix[mid][0]:
                l=mid+1
            else:
                return True
        if(target<matrix[mid][0]):
            i=mid-1
        elif(target>matrix[mid][0]): 
            i=mid
        else:
            return True
            
        newl,newr=0,len(matrix[0])-1
        while(newl<=newr):
            mid=(newl+newr)//2
            if target<matrix[i][mid]:
                newr=mid-1
            elif target>matrix[i][mid]:
                newl=mid+1
            else:
                return True
        return False
            