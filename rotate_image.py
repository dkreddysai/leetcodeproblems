# Rotate Image
class Solution:
    def rotate(matrix):
        rotate_mat = []
        for l in range(len(matrix)):
            mat = [i[l] for i in matrix][::-1]
            rotate_mat.append(mat)
        return rotate_mat
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(matrix))
    
