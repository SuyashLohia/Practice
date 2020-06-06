class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]  
                
    """
    1) def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
    
    2) def rotate(self, A):
        A[:] = map(list, zip(*A[::-1]))
    
    3) def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                for _ in '123':
                    A[i][j], A[~j][i], i, j = A[~j][i], A[i][j], ~j, ~i
                i = ~j
    """