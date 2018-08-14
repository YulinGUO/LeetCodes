__author__ = 'yulin'
'''
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
'''


class FSLGTT(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s = 0
        l = len(letters) - 1
        while s <= l:
            m = l + (s - l) / 2
            if letters[m] <= target:
                s = m + 1
            else:
                l = m - 1
        return letters[s] if s < len(letters) else letters[0]

def main():
    fslgtt = FSLGTT()
    print(fslgtt.nextGreatestLetter(["c", "f", "j"], 's'))


if __name__ == '__main__':
    main()
