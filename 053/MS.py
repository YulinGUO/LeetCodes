__author__ = 'yulin'
'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
'''


class MS(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n > 0:
            pre_sum = nums[0]
            max_sum = pre_sum
            for i in range(1, n):
                pre_sum = pre_sum + nums[i] if pre_sum > 0 else nums[i]
                max_sum = max(pre_sum, max_sum)
            return max_sum
        else:
            return 0


def main():
    ms = MS()
    print(ms.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    main()
