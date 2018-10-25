__author__ = 'yulin'
'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTP(object):
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #
    #     res = []
    #
    #     def preorderTraversalTail(root):
    #         if root is not None:
    #             res.append(root.val)
    #             preorderTraversalTail(root.left)
    #             preorderTraversalTail(root.right)
    #
    #     preorderTraversalTail(root)
    #
    #     return res

    # iteratively
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        stack = []

        def preorderTraversalTail(root):
            if root is not None:
                stack.append(root)

            while len(stack) > 0:
                node = stack.pop()
                if node is not None:
                    res.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)

        preorderTraversalTail(root)

        return res


def main():
    btp = BTP()

    a = TreeNode(1)
    a1 = TreeNode(2)
    b = TreeNode(3)

    a1.left = b
    a.right = a1

    print(btp.preorderTraversal(a))


if __name__ == '__main__':
    main()
