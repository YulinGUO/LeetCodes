__author__ = 'yulin'
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
import string

class LCPN(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitletter = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def combine(com, digits, res):
            if len(com) == len(digits):
                res.append(com)
            else:
                letters = digitletter[int(digits[len(com)])]
                for letter in letters:
                    combine(com+letter, digits, res)

        res = []
        if len(digits) > 0:
            combine("", digits, res)

        return res

def main():
    lcpn = LCPN()
    print(lcpn.letterCombinations("234"))


if __name__ == '__main__':
    main()
