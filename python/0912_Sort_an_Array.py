class Solution:
    def partition(self,nums,L,R):
        less=L-1
        more=R

        while(L<more):
            if(nums[L]<nums[R]):
                less+=1
                nums[less],nums[L]=nums[L],nums[less]
                L+=1
            elif(nums[L]>nums[R]):
                more-=1
                nums[more],nums[L]=nums[L],nums[more]
            else:
                L+=1

        nums[more],nums[R]=nums[R],nums[more]
        return [less+1,more]

    def sort(self,nums,L,R):
        if(L<R):
            p=self.partition(nums,L,R)
            self.sort(nums,L,p[0]-1)
            self.sort(nums,p[1]+1,R)

    def sortArray(self, nums):
        self.sort(nums,0,len(nums)-1)
        return nums