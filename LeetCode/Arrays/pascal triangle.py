class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """if numRows==0:
            return[]
        if numRows==1:
            return [[1]]
        pr=self.generate(numRows-1)
        nr=[1]*numRows
        for i in range(1,numRows-1):
            nr[i]=pr[-1][i-1]+pr[-1][i]
        pr.append(nr)
        return pr  """
        tri=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=tri[i-1][j-1]+tri[i-1][j]
            tri.append(r)
        return tri
