__author__ = 'yulin'
'''
Friend Circles
https://leetcode.com/problems/friend-circles/description/
'''
from collections import deque


class FS(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        stack = deque([])
        stack.append(0)
        visited = [False for _ in range(len(M))]
        visited[0] = True
        circles = 0
        while stack:
            print(stack)
            i = stack.pop()
            for j in range(len(M[i])):
                if visited[j] or i == j or M[i][j] == 0:
                    continue
                else:
                    stack.append(j)
                    visited[j] = True

            if not stack:
                circles += 1
                if sum(visited) < len(M):
                    idx = visited.index(False)
                    stack.append(idx)
                    visited[idx] = True
        return circles


def main():
    fs = FS()
# [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    M = list([list([1,0,0,1]), list([0,1,1,0]), list([0,1,1,1]),list([1,0,1,1])])
    print(fs.findCircleNum(M))


if __name__ == '__main__':
    main()
