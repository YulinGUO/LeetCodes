__author__ = 'yulin'
'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

### bucket sort
from collections import Counter, defaultdict


class SCBF(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        res = []
        invers_freq = defaultdict(list)
        for key, vv in freq.items():
            invers_freq[vv].append(key)

        for x in range(len(s), -1, -1):
            if x in invers_freq:
                for letter in invers_freq[x]:
                    res.extend(x * [letter])

        return ''.join(res)


def main():
    scbf = SCBF()
    print(scbf.frequencySort(""))


if __name__ == '__main__':
    main()
