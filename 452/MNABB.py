__author__ = 'yulin'

'''
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart <= x <= xend.
 There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely.
 The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6])
 and another arrow at x = 11 (bursting the other two balloons).
'''


class MNABB(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 1
        if len(points) > 0:
            spoints = sorted(points, key=lambda x: (x[0], x[1]))
            print(''.join([''.join(str(x)) for x in spoints]))
            i = 0
            ba = spoints[0][0]
            bb = spoints[0][1]
            while i < len(points) - 1:
                if bb >= spoints[i + 1][0]:
                    ba = max(ba, spoints[i + 1][0])
                    bb = min(bb, spoints[i + 1][1])
                    i += 1
                else:
                    cnt += 1
                    ba = spoints[i + 1][0]
                    bb = spoints[i + 1][1]
                    i += 1
        else:
            return 0

        return cnt


def main():
    mnabb = MNABB()
    print(mnabb.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))


if __name__ == '__main__':
    main()
