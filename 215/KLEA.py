__author__ = 'yulin'
'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 <= k <= array's length.
'''


class KLEA(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quickSort(nums, l, r):

            i = l
            j = r
            # print('------ i % r j% r' % (i, j))
            if i < j:
                tmp = nums[i]
                while i < j:
                    while i < j and nums[j] <= tmp:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1

                    while i < j and nums[i] >= tmp:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                nums[i] = tmp
                # print('stop at i %r' % i)
                # print(nums)
                quickSort(nums, l, i - 1)
                quickSort(nums, i + 1, r)

        i = 0
        j = len(nums) - 1
        quickSort(nums, i, j)
        print(nums)
        return nums[k - 1]

        # quick sort functions


def main():
    klea = KLEA()
    print(klea.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


if __name__ == '__main__':
    main()
