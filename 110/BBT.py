__author__ = 'yulin'
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BBT(object):
    bal = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def get_height(root):
            if root is not None:
                if root.left is None and root.right is None:
                    return 1
                l_height = get_height(root.left)
                r_height = get_height(root.right)

                if abs(l_height - r_height) > 1:
                    self.bal = False
                return max(l_height, r_height) + 1
            else:
                return 0

        get_height(root)
        return self.bal


def main():
    bbt = BBT()

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

    print(bbt.isBalanced(e))


if __name__ == '__main__':
    main()
