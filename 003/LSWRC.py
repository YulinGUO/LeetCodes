#!/usr/bin/python2
__author__ = 'yulin'

"""
003
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class LSWRC(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        i = 0
        j = 0
        maxLen = 0
        length = len(s)
        while i < length and j < length:
            if s[j] not in charSet:
                charSet.add(s[j])
                j += 1
                maxLen = max(maxLen, j - i)
            else:
                charSet.remove(s[i])
                i += 1
        return maxLen


def main():
    lswrc = LSWRC()
    lswrc.lengthOfLongestSubstring('abcabcbb')
    lswrc.lengthOfLongestSubstring('bbbbb')
    lswrc.lengthOfLongestSubstring('pwwkew')


if __name__ == '__main__':
    main()
