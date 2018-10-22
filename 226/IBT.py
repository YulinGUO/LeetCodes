__author__ = 'yulin'
'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class IBT(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            if root.left is None and root.right is None:
                return root

            tmp = root.left
            root.left = root.right
            root.right = tmp

            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


def main():
    ibt = IBT()

    a = TreeNode(15)
    a1 = TreeNode(150)
    b = TreeNode(7)
    c = TreeNode(9)
    d = TreeNode(20)
    e = TreeNode(3)

    a.left = a1

    d.left = a
    d.right = b

    e.left = c
    e.right = d


    ibt.invertTree(e)

if __name__ == '__main__':
    main()


