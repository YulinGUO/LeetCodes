__author__ = 'yulin'
'''
Given a list of daily temperatures T, return a list such that, for each day in the input,
 tells you how many days you would have to wait until a warmer temperature.
 If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
 your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''


class DT(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        dist = [0] * len(T)
        stack = []

        for i in range(0, len(T)):

            while stack and T[i] > T[stack[-1]]:
                pre_index = stack.pop()
                dist[pre_index] = i - pre_index

            stack.append(i)

        return dist


def main():
    dt = DT()
    print(dt.dailyTemperatures([]))


if __name__ == '__main__':
    main()
