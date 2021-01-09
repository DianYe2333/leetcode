class Solution:
    def findDiagonalOrder(self, matrix):
        res=[]

        if(len(matrix)==0):
            return res

        aR=0
        aC=0
        bR=0
        bC=0
        endR=len(matrix)-1
        endC=len(matrix[0])-1
        turn=False

        while(not aR==endR+1):
            self.helper(matrix,res,turn,aR,aC,bR,bC)
            aR=aR if(not aC==endC) else aR+1
            aC=aC if(aC==endC) else aC+1
            bC=bC if(not bR==endR) else bC+1
            bR=bR if(bR==endR) else bR+1
            turn=not turn

        return res


    def helper(self,matrix,res,turn,aR,aC,bR,bC):
        if(turn):
            #turn为True，则顺时针打印
            while(not aR==bR+1):
                res.append(matrix[aR][aC])
                aR+=1
                aC-=1
        else:
            while(not bR==aR-1):
                res.append(matrix[bR][bC])
                bR-=1
                bC+=1

