class MyQueue(object):

    def __init__(self):
        self.l1 = []
        self.l2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.l1:
            self.l2.append(self.l1.pop())
        self.l1.append(x)
        
        while self.l2:
            self.l1.append(self.l2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.l1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.l1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.l1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()