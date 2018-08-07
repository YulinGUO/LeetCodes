__author__ = 'yulin'
'''
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return 'start %r end %r' % (self.start, self.end)


class NOI(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        cnt = 1
        res = 0
        if len(intervals) > 0:
            sint = sorted(intervals, key=lambda x: x.end)
            si = 0
            sj = 1
            while si < len(sint) and sj < len(sint):
                if sint[si].end <= sint[sj].start:
                    cnt += 1
                    si = sj

                sj += 1

            res = len(sint) - cnt
        return res


def main():
    noi = NOI()
    a = [Interval(1, 2), Interval(2, 3)]
    b = [Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(1, 3)]
    c = [Interval(1, 2), Interval(1, 2), Interval(1, 2)]
    print(noi.eraseOverlapIntervals(a))
    print(noi.eraseOverlapIntervals(b))
    print(noi.eraseOverlapIntervals(c))
    # //[[1,100],[11,22],[1,11],[2,12]]
    d = [Interval(1, 100), Interval(11, 22), Interval(1, 11), Interval(2, 12)]
    print(noi.eraseOverlapIntervals(d))


if __name__ == '__main__':
    main()
