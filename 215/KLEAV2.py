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


class KLEAV2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def mergeSort(nums):
            if len(nums) > 1:
                middle = len(nums) / 2
                left = mergeSort(nums[:middle])
                right = mergeSort(nums[middle:])
                return merge(left, right)
            else:
                return nums

        def merge(left, right):
            i = 0
            j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            if i == len(left):
                res.extend(right[j:])
            else:
                res.extend(left[i:])
            return res

        print('nums')
        print(nums)
        nnums = mergeSort(nums)
        print(nnums)
        return nnums[k - 1]


def main():
    klea = KLEAV2()
    print(klea.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


if __name__ == '__main__':
    main()
