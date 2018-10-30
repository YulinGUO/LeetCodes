__author__ = 'yulin'
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.smin = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.smin:
            self.smin.append(x)
        else:
            self.smin.append(min(self.smin[-1], x))
        self.s1.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.smin.pop()
        self.s1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.smin[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    obj = MinStack()
    obj.push(-1)
    obj.push(-3)
    # print(obj.pop())
    #
    # print(obj.peek())
    # print(obj.pop())
    print(obj.getMin())
    obj.push(2)
    print(obj.getMin())
    print(obj.top())
    print(obj.pop())
    print(obj.top())
    print(obj.pop())
    print(obj.getMin())



if __name__ == '__main__':
    main()
