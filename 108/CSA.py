__author__ = 'yulin'
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CSA(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.__to_bst(nums, 0, len(nums)-1)

    def __to_bst(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        mid_node = TreeNode(nums[mid])
        mid_node.left = self.__to_bst(nums, start, mid - 1)
        mid_node.right = self.__to_bst(nums, mid + 1, end)
        return mid_node


def main():
    csa = CSA()
    nums = [1, 2, 3, 4, 5, 6]
    print(csa.sortedArrayToBST(nums).right.val)


if __name__ == '__main__':
    main()
