__author__ = 'yulin'

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 < = k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class KSE(object):
    res = 0
    count = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorderBT(root, k)
        return self.res

    def inorderBT(self, root, k):
        if root is None:
            return
        self.inorderBT(root.left, k)
        tmp = root.val
        self.count += 1
        if self.count == k:
            self.res = tmp
            return
        self.inorderBT(root.right, k)


def main():
    kse = KSE()

    a = TreeNode(1)
    a1 = TreeNode(2)
    b = TreeNode(3)
    b1 = TreeNode(0)

    a1.right = b
    a.right = a1
    a.left = b1

    print(kse.kthSmallest(a,1))


if __name__ == '__main__':
    main()
