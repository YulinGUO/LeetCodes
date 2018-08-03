__author__ = 'yulin'

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:

Assume we are dealing with an environment
 which could only store integers within the 32-bit
 signed integer range: [-2**31,2**31-1]
  For the purpose of this problem,
  assume that your function returns 0
  when the reversed integer overflows.

'''


class RI(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # system 64 : maxInt:sys.maxsize=9223372036854775807
        maxInt = 2147483647
        res = 0
        flag = 1 if x>=0 else -1
        x=abs(x)
        while x is not 0:
            pop = x % 10
            x /= 10

            if res > maxInt / 10 or (res == maxInt / 10 and pop > 7):
                return 0

            res = res * 10 + pop
        return res*flag

def main():
    ri = RI()
    print(ri.reverse(-123))
    print(ri.reverse(90))
    print(ri.reverse(0))

if __name__ == '__main__':
    main()
