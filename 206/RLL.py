__author__ = 'yulin'
'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

import copy


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RLL(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        next = head.next
        aa = self.reverseList(next)
        next.next = head
        head.next = None
        return aa


def main():
    rll = RLL()

    a1 = ListNode(1)
    a2 = ListNode(2)
    b1 = ListNode(11)
    c1 = ListNode(102)

    a1.next = a2
    a2.next = b1
    b1.next = c1
    #
    # tmp = a1
    # while tmp is not None:
    #     print(tmp.val)
    #     tmp = tmp.next

    cc = rll.reverseList(a1)

    while cc is not None:
        print(cc.val)
        cc = cc.next


if __name__ == '__main__':
    main()
