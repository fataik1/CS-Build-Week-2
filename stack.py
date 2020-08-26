'''
Queue FIFO
Stack FILO
[1,2,3]

[3,2,1]

'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inn = []
        self.out = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inn.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.out.pop()
        


    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inn and not self.out
        
    def move(self):
        #pop out values from in stack & append
        if not self.out:
            while self.inn:
                self.out.append(self.inn.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()