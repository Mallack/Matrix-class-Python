import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 2:
            return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        
        if self.h == 1:
            return self.g[0][0]
        
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sumM = 0
        for i in range(self.h):
            sumM = sumM + self.g[i][i] 
                    
        return sumM
    
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            inv_Matrix = zeroes(1,1)
            inv_Matrix[0][0] = 1/self.g[0][0]
            return inv_Matrix
        
        if self.h == 2:
            inv_Matrix = zeroes(2, 2)
            x = 1/self.determinant()
            inv_Matrix[0][0] = x * self.g[1][1]
            inv_Matrix[0][1] = x * -self.g[0][1]
            inv_Matrix[1][0] = x * -self.g[1][0]
            inv_Matrix[1][1] = x * self.g[0][0]
            return inv_Matrix
        
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        MatrixT = zeroes(self.w,self.h)
        for j in range(self.w):
            for i in range(self.h):
                MatrixT[j][i] = self.g[i][j]
        return MatrixT

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]
        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        MatrixSUM = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                MatrixSUM[i][j] = self.g[i][j]+other.g[i][j]
        return MatrixSUM
        
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        Example:
        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        MatrixN = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                MatrixN[i][j] = - self.g[i][j]
        return MatrixN

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        subM=zeroes(self.h,self.w)
        for i in range(self.h): 
            for j in range(self.w): 
                subM[i][j] = self.g[i][j]-other.g[i][j]
        return  subM

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        
        mul = zeroes(self.h,other.w)
        Transpose = other.T()
        for i in range (self.h):
            for j in range (Transpose.h):
                mul[i][j] = dot_product(self.g[i],Transpose.g[j]) 
        return mul
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.
        Example:
        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            Rmul = zeroes(self.h,self.w)
            for i in range(self.h):
                for j in range(self.w):
                    Rmul[i][j] = (other*self.g[i][j])
            return Rmul

        
        
def dot_product(v1, v2):
    x = 0
    for i in range(len(v1)):
        x += v1[i] * v2[i]
    return x