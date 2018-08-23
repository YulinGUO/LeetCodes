__author__ = 'yulin'
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MKSL(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)

        skip = 1

        while skip < amount:
            for i in range(0, amount - skip, skip * 2):
                lists[i] = self.merge_2_list(lists[i], lists[i + skip])

            skip *= 2
        return lists[0] if amount > 0 else lists

    def merge_2_list(self, left, right):
        head = ListNode(0)
        point = head

        while left and right:
            if right.val <= left.val:
                point.next = right
                right = right.next
            else:
                point.next = left
                left = left.next

            point = point.next

        if left:
            point.next = left

        if right:
            point.next = right

        return head.next


def main():
    mksl = MKSL()

    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    aa = ListNode(1)
    bb = ListNode(3)
    cc = ListNode(4)

    aa.next = bb
    bb.next = cc

    aaa = ListNode(2)
    bbb = ListNode(6)

    aaa.next = bbb

    # res = mksl.merge_2_list(a, aa)
    # print(len(res))
    lists = list([a, aa, aaa])
    res = mksl.mergeKLists(lists)

    while res:
        print(res.val)
        res = res.next


if __name__ == '__main__':
    main()
