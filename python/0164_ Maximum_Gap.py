import sys

MAX_INT=sys.maxsize
MIN_INT=-sys.maxsize - 1

class Solution:
    def maximumGap(self, nums) -> int:
        if(len(nums)<2):
            return 0

        l=len(nums)
        Min=MAX_INT
        Max=MIN_INT

        for i in range(l):
            Min=min(Min,nums[i])
            Max=max(Max,nums[i])

        if(Min==Max):
            return 0

        has_nums=[False]*(l+1)
        maxs=[None]*(l+1)
        mins=[None]*(l+1)

        for i in range(l):
            bid=self.bucket(nums[i],l,Min,Max)
            mins[bid]=min(mins[bid],nums[i]) if has_nums[bid] else nums[i]
            maxs[bid] = max(maxs[bid], nums[i]) if has_nums[bid] else nums[i]
            has_nums[bid]=True

        res=0
        last_max=maxs[0]
        for i in range(1,l+1):
            if has_nums[i]:
                res=max(res,mins[i]-last_max)
                last_max=maxs[i]

        return res

    def bucket(self,num,l,Min,Max):
        return int((num-Min)*l/(Max-Min))