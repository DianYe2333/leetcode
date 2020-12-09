from random import random


def quick_sorts(left,right,nums):
    #传统快速排序
    if(left>right):
        return
    i=left
    j=right
    base=nums[left]
    while(i<j):
        while(nums[j]>=base and i<j):
            j-=1
        while(nums[i]<=base and i<j):
            i+=1
        if(i<j):
            nums[i],nums[j]=nums[j],nums[i]

    nums[left],nums[i]=nums[i],base
    quick_sorts(left,i-1,nums)
    quick_sorts(i+1,right,nums)

    return nums


def quick_sorts_2(nums,L,R):
    #基于荷兰国旗问题的改进版（左神初级算法课02)
    if(L<R):
        #随机快排：随机将数组中一个位置与数组末尾位置的数交互
        rd=int(random()*(R-L+1))
        swap(nums,L+rd,R)

        p=partition(nums,L,R)
        quick_sorts_2(nums,L,p[0]-1)
        quick_sorts_2(nums,p[1]+1,R)


def partition(nums,L,R):
    #分治
    less=L-1
    more=R
    while(L<more):
        if(nums[L]<nums[R]):
            less+=1
            #nums[less],nums[L]=nums[L],nums[less]
            swap(nums,less,L)
            L+=1
        elif(nums[L]>nums[R]):
            more-=1
            #nums[more],nums[L]=nums[L],nums[more]
            swap(nums,more,L)
        else:
            L+=1

    #nums[R]作为base，所以最后将nums[R]放到数组中间位置
    swap(nums,more,R)
    #nums[more],nums[R]=nums[R],nums[more]

    return [less+1,more]


def swap(nums,i,j):
    nums[i],nums[j]=nums[j],nums[i]

if __name__=="__main__":
    l=[1,3,2,1,5,2,66,22,77]
    quick_sorts_2(l,0,len(l)-1)
    print(l)