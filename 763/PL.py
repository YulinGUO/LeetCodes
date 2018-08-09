__author__ = 'yulin'
'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible
 so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''


class PL(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        cnt = []
        if len(S) > 0:
            # construct (letter,last_appears)
            sappaers = {letter: num for num, letter in enumerate(S)}
            i = 0
            j = 0
            lst = 0
            while i < len(S):
                j = sappaers.get(S[i])
                i += 1
                while i <= j:
                    j = max(j, sappaers.get(S[i]))
                    i += 1
                cnt.append(j+1-lst)
                lst = j+1

        return cnt


def main():
    pl = PL()
    print(pl.partitionLabels("ababcbacadefegdehijhklij"))

if __name__ == '__main__':
    main()
