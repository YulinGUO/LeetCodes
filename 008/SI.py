__author__ = 'yulin'
'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers
 within the 32-bit signed integer range:  If the numerical value is out of
 the range of representable values, INT_MAX Or INT_MIN is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN  is returned.
'''


class SI(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        def flatInt(i):
            maxInt = 2147483647
            minInt = -2147483648
            if i > maxInt:
                return maxInt
            if i < minInt:
                return minInt
            return i

        res = 0
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flags = ['-', '+']
        flag = 1
        if len(str) > 0:
            j = 0
            if str[j] in flags:
                flag = -1 if str[j] == '-' else 1
                # string comparision : use == or is???
                j += 1
            while j < len(str) and str[j] in num:
                res = res * 10 + int(str[j])
                j += 1

        return flatInt(flag * res)


def main():
    si = SI()
    print(si.myAtoi("+1"))
    print(si.myAtoi('   -42'))
    print(si.myAtoi('   +42'))
    print(si.myAtoi('   +42   s34'))
    print(si.myAtoi('   w+42   s34'))

if __name__ == '__main__':
    main()
