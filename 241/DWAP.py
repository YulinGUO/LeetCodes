__author__ = 'yulin'
'''
Given a string of numbers and operators,
return all possible results from computing
all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
'''


class DWAP(object):
    def diffWaysToCompute(self, input):
        print('*' * len(input) * 3)
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            print('input:' + input[i:])
            if input[i] in "-+*":
                print('will cal left: ' + input[:i])
                res1 = self.diffWaysToCompute(input[:i])
                print('will cal right: ' + input[i + 1:])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
                        print(str(j) + str(k) + input[i])
                print(res)
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n


def main():
    dwap = DWAP()
    print(dwap.diffWaysToCompute('2*3-4*5'))


if __name__ == '__main__':
    main()
