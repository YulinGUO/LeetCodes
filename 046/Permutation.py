__author__ = 'yulin'
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
import copy


class Permutation(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def perm(pers_old, nums, res):
            pers = copy.deepcopy(pers_old)
            if len(pers) == len(nums):
                res.append(pers)
            else:
                for one in nums:
                    if one in pers:
                        continue
                    pers.append(one)
                    perm(pers, nums, res)
                    pers.remove(one)

        if len(nums) > 0:
            perm([], nums, res)
        return res


def main():
    perm = Permutation()
    print(perm.permute(list([1, 2, 3])))


if __name__ == '__main__':
    main()
