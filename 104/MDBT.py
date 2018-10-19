__author__ = 'yulin'
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3

'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MDBT(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is not None:
            if root.left is None and root.right is None:
                return 1

            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0


def main():
    mdbt = MDBT()

    a = TreeNode(15)
    b = TreeNode(7)
    c = TreeNode(9)
    d = TreeNode(20)
    e = TreeNode(3)

    d.left = a
    d.right = b

    e.left = c
    e.right = d

    print(mdbt.maxDepth(e))


if __name__ == '__main__':
    main()
