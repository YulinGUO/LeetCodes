__author__ = 'yulin'
'''
Write a program to find the node at which the intersection of two singly linked lists begins.



Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ITLL(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = headA
        lb = headB
        while la is not lb:
            la = headB if la is None else la.next
            lb = headA if lb is None else lb.next

        return la


def main():
    itll = ITLL()

    a1 = ListNode(1)
    a2 = ListNode(2)

    b1 = ListNode(11)

    c1 = ListNode(102)

    a1.next = a2
    a2.next=c1

    b1.next=c1

    print(itll.getIntersectionNode(a1,b1).val)


if __name__ == '__main__':
    main()
