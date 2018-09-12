__author__ = 'yulin'
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class ClimbS(object):
    '''
    v1: brute force
     Time Limit Exceeded
    '''

    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #
    #     def climb(i, n):
    #         if i > n:
    #             return 0
    #         if i == n:
    #             return 1
    #         else:
    #             return climb(i + 1, n) + climb(i + 2, n)
    #
    #     return climb(0, n)

    '''
    v2: brute force with memory
    '''
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     tmp = [-1] * n
    #
    #     def climb(i, n, tmp):
    #         if i > n:
    #             return 0
    #         if i == n:
    #             return 1
    #         if tmp[i] > 0:
    #             return tmp[i]
    #         else:
    #             tmp[i] = climb(i + 1, n, tmp) + climb(i + 2, n, tmp)
    #             return tmp[i]
    #
    #     return climb(0, n, tmp)

    '''
    dynamic programming
    '''

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dm = [-1]*(n+2)
        dm[1] = 1
        dm[2] = 2

        i = 3
        while i <= n:
            dm[i] = dm[i - 1] + dm[i - 2]
            i += 1
        return dm[n]


def main():
    climb = ClimbS()
    print(climb.climbStairs(4))


if __name__ == '__main__':
    main()
