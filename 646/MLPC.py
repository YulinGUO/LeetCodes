__author__ = 'yulin'
'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
'''


class MLPC(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sort_pair = sorted(pairs, key=lambda x: x[1])
        print(sort_pair)
        max_len = 1
        for i in range(len(sort_pair)):
            pre_len = 1
            cur = sort_pair[i][1]
            for j in range(i + 1, len(sort_pair)):
                if sort_pair[j][0] > cur:
                    pre_len += 1
                    max_len = max(pre_len, max_len)
                    cur = sort_pair[j][1]
                j += 1
            i += 1
        return max_len

def main():
    mlpc = MLPC()
    print(mlpc.findLongestChain([[-1,1],[-2,7],[-5,8],[-3,8],[1,3],[-2,9],[-5,2]]))


if __name__ == '__main__':
    main()

