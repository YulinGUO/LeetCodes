__author__ = 'yulin'
'''
You are a product manager and currently leading a team to develop a new product.
 Unfortunately, the latest version of your product fails the quality check.
 Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
 which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
'''


class FBV(object):
    # def isBadVersion(n):
    #     return True if n <= 3 else False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def isBadVersion(n):
            return True if n >=6 else False

        s = 1
        h = n

        while s < h:
            m = s + (h - s) / 2
            if isBadVersion(m):
                h = m
            else:
                s = m + 1

        return s


def main():
    fbv = FBV()
    print(fbv.firstBadVersion(9))


if __name__ == '__main__':
    main()
