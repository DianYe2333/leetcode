class Solution:
    def spiralOrder(self, matrix):
        res = []
        tR=0
        tC=0
        dR=len(matrix)-1
        dC=len(matrix[0])-1

        while(tR<=dR and tC<=dC):
            self.helper(res,matrix,tR,tC,dR,dC)
            tR+=1
            tC+=1
            dR-=1
            dC-=1

        return res

    def helper(self,res,matrix,tR,tC,dR,dC):
        if(tR==dR):
            while(tC<=dC):
                res.append(matrix[tR][tC])
                tC+=1
        elif(tC==dC):
            while(tR<=dR):
                res.append(matrix[tR][tC])
                tR+=1
        else:
            curC=tC
            curR=tR
            while(curC!=dC):
                res.append(matrix[tR][curC])
                curC+=1

            while(curR!=dR):
                res.append(matrix[curR][dC])
                curR+=1

            while(curC!=tC):
                res.append(matrix[dR][curC])
                curC-=1

            while(curR!=tR):
                res.append(matrix[curR][tC])
                curR-=1
