__author__ = 'yulin'

'''

005
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Dynamic Programming
'''


class LPS(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = len(s)

        def findBasciPalindrome(s):
            i = 0
            pals = []
            while i <= (ls - 2):
                if s[i] == s[i + 1]:
                    pals.append([i, i + 1])
                if i + 2 < ls and s[i + 2] == s[i]:
                    pals.append([i, i + 2])
                i += 1

            return pals

        maxLen = 0
        maxI = 0
        maxJ = 0
        pals = findBasciPalindrome(s)
        print(pals)

        for ti, tj in pals:
            print('---------------------------')
            print('begin ti %r tj %r' % (ti,tj))
            if maxLen < tj - ti + 1:
                print('first maxLen %r' % maxLen)
                maxI = ti
                maxJ = tj
                maxLen = tj - ti + 1
            ti -= 1
            tj += 1
            while ti > -1 and tj < ls:
                if s[ti] == s[tj]:
                    print('same added')
                    ti -= 1
                    tj += 1
                    print(' ti %r  tj %r' % (ti,tj))
                else:
                    break
            ti += 1
            tj -= 1
            if maxLen < tj - ti + 1:
                maxI = ti
                maxJ = tj
                maxLen = tj - ti + 1

        return s[maxI:maxJ+1]


def main():
    lps = LPS()
    print(lps.longestPalindrome('ababababa'))



if __name__ == '__main__':
    main()
