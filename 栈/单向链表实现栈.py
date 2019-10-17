class LinkedStack:
    class _Node:
    #定义一个私有结构
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        answer = self._head._element
        self._head = self._head._next       #链表指向下一个内容，间接删除头部元素
        self._size -= 1
        return answer
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element
