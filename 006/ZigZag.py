__author__ = 'yulin'

'''
006
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class ZigZag(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = [[] for i in range(numRows)]

        j = 0

        direction = 0
        steps_done = 0
        steps_dtwo = 0
        max_steps_done = numRows
        max_steps_dtwo = numRows - 2
        while j < len(s):
            print('---------------------------')
            if direction is 0:
                print(direction)
                if steps_done < max_steps_done:
                    res[steps_done].append(s[j])

                    j += 1
                    steps_done += 1

                    if steps_done == max_steps_done:
                        direction = 1

                steps_done %= max_steps_done

            else:
                if max_steps_dtwo>0:
                    print(direction)
                    if steps_dtwo < max_steps_dtwo:
                        res[numRows - steps_dtwo - 2].append(s[j])
                        j += 1
                        steps_dtwo += 1
                        if steps_dtwo == max_steps_dtwo:
                            direction = 0

                    steps_dtwo %= max_steps_dtwo
                else:
                    direction = 0

        return ''.join([''.join(one) for one in res])


def main():
    zig = ZigZag()
    print(zig.convert('ABC', 2))


if __name__ == '__main__':
    main()
