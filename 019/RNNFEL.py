__author__ = 'yulin'
'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class RNNFEL(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head

        while n > 0 and fast is not None and fast.next is not None:
            fast = fast.next
            n -= 1

        if n>0:
            return slow.next

        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next if slow.next is not None else None

        return head

def main():

    rnnfel = RNNFEL()

    a1 = ListNode(1)
    # a2 = ListNode(2)
    #
    # b1 = ListNode(11)
    #
    # c1 = ListNode(102)
    #
    # a1.next = a2
    # a2.next=b1
    # b1.next=c1

    cc = a1

    while cc is not None:
        print(cc.val)
        cc = cc.next

    print('*'*10)
    dd = a1
    ee = rnnfel.removeNthFromEnd(dd,1)

    while ee is not None:
        print(ee.val)
        ee = ee.next


if __name__ == '__main__':
    main()
