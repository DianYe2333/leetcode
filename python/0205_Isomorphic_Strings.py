class Solution:
    def isIsomorphic(self,s,t):
        s2t=dict()
        t2s=dict()

        for i in range(len(s)):
            x=s[i]
            y=t[i]
            if((x in s2t and s2t[x]!=y) or (y in t2s and t2s[y]!=x)):
                return False

            s2t[x]=y
            t2s[y]=x

        return True