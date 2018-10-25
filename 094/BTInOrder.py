__author__ = 'yulin'
'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BTInOrder(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def inorderTraversalTail(root):
            if root is not None:

                inorderTraversalTail(root.left)
                res.append(root.val)
                inorderTraversalTail(root.right)

        inorderTraversalTail(root)

        return res

def main():
    btin = BTInOrder()

    a = TreeNode(1)
    a1 = TreeNode(2)
    b = TreeNode(3)

    a1.left = b
    a.right = a1

    print(btin.inorderTraversal(a))

if __name__ == '__main__':
    main()