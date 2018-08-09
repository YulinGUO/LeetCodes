__author__ = 'yulin'
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LLC(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        else:
            i = head
            j = head
            while j.next is not None and j.next.next is not None:
                j = j.next.next
                i = i.next
                if j.val is i.val:
                    return True
            return False


def main():
    llc = LLC()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    print(llc.hasCycle(a))


if __name__ == '__main__':
    main()
