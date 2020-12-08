class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        L = -1
        R = len(nums)

        while (cur < R):
            if (nums[cur] == 1):
                cur += 1
            elif (nums[cur] < 1):
                L += 1
                nums[cur], nums[L] = nums[L], nums[cur]
                cur += 1
            else:
                R -= 1
                nums[cur], nums[R] = nums[R], nums[cur]
