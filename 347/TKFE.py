__author__ = 'yulin'
'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
### bucket sort
from collections import Counter, defaultdict


class TKFE(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        res = []
        inverse_freq = defaultdict(list)
        for key, vv in freq.items():
            inverse_freq[vv].append(key)
        print(inverse_freq)
        for x in range(len(nums), 0, -1):
            if x in inverse_freq.keys():
                res.extend(inverse_freq[x])
                if len(res) >= k:
                    break
        return res[:k]


def main():
    tkfe = TKFE()
    print(tkfe.topKFrequent([1, 1, 3,1,4, 2, 2, 3], 2))


if __name__ == '__main__':
    main()
