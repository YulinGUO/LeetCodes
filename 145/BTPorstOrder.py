__author__ = 'yulin'
'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTPorstOrder(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def postorderTraversalTail(root):
            if root is not None:

                postorderTraversalTail(root.left)
                postorderTraversalTail(root.right)
                res.append(root.val)

        postorderTraversalTail(root)

        return res


def main():
    btporst = BTPorstOrder()

    a = TreeNode(1)
    a1 = TreeNode(2)
    b = TreeNode(3)

    a1.left = b
    a.right = a1

    print(btporst.postorderTraversal(a))

if __name__ == '__main__':
    main()