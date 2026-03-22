class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def transpoe(matrix):
            transposed=[]
            for i in range(len(matrix)):
                trans=[]
                for j in range(len(matrix[0])):  
                    trans.append(matrix[j][i])
                transposed.append(trans)
            return transposed

        def rev(mat):
            for i in mat:
                i.reverse()
            return mat
        n=0
        while n <4:
            mat=transpoe(mat)
            mat=rev(mat)
            n+=1
            if mat == target:
                return True
        

        return False