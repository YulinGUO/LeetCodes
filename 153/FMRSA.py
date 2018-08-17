__author__ = 'yulin'
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''


class FMRSA(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        h = len(nums) - 1
        while s < h:
            m = s + (h - s) / 2
            if nums[m] <= nums[h]:
                h = m
            else:
                s = m + 1
        return nums[s]


def main():
    fmrsa = FMRSA()
    print(fmrsa.findMin([4, 5, 6, 7, 0, 1, 2]))


if __name__ == '__main__':
    main()
