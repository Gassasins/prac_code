#rotate image


import os
import sys

class rt_img:
    def rt1(self,mat):
        print(mat)
        x = len(mat)
        for i in range(x):
            for j in range(i+1,x):
                if i == j:
                    continue
                else:
                    tmp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = tmp
        self.rt2(mat)
    
    def rt2(self, mat):
        print(mat)
        x = len(mat)
        for i in range(x):
            for j in range(x//2):
                # print(x,i,j)
                tmp = mat[i][j]
                mat[i][j] = mat[i][x-j-1]
                mat[i][x-j-1] = tmp
        print(mat)
                

val1=[[1,2,3],[4,5,6],[7,8,9]]
val2=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
at = rt_img()
at.rt1(val1)
at.rt1(val2)
        