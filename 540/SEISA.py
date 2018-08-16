__author__ = 'yulin'
'''
Given a sorted array consisting of only integers
where every element appears twice except for one element which appears once.
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
'''


class SEISA(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        h = len(nums) - 1
        while s < h:
            m = s + (h - s) / 2
            if m % 2 is 1:
                m -= 1
            if nums[m] < nums[m + 1]:
                h = m
            else:
                s = m + 2
        return nums[s]


def main():
    seisa = SEISA()
    print(seisa.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))


if __name__ == '__main__':
    main()
