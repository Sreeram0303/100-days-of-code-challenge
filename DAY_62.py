# class Stack:
    
#     def __init__(self, capacity: int):
#         # Write your code here.
#         self.capacity = capacity
#         self.stack = deque()

#     def push(self, num: int) -> None:
#         # Write your code here.
#         if not self.isFull():
#            self.stack.append(num)
#         return -1
        

#     def pop(self) -> int:
#         # Write your code here.
#         if self.isEmpty():
#             return -1
#         return self.stack.pop()
    
#     def top(self) -> int:
#         # Write your code here.
#         if self.isEmpty():
#             return -1
#         return self.stack[-1]
    
#     def isEmpty(self) -> int:
#         # Write your code here.
#         if len(self.stack) == 0:
#             return 1
#         return 0
            
    
#     def isFull(self) -> int:
#         # Write your code here.
#         if len(self.stack) == self.capacity:
#             return 1
#         return 0


# class Queue:
#     def __init__(self):
#         self.start = -1
#         self.end = -1
#         self.currSize = 0
#         self.maxSize = 16
#         self.arr = [0] * self.maxSize


#     def push(self, newElement: int) -> None:
#         if self.currSize == self.maxSize:
#             print("Queue is full\nExiting...")
#             exit(1)
#         if self.end == -1:
#             self.start = 0
#             self.end = 0
#         else:
#             self.end = (self.end + 1) % self.maxSize
#         self.arr[self.end] = newElement
#         print("The element pushed is", newElement)
#         self.currSize += 1


#     def pop(self) -> int:
#         if self.start == -1:
#             print("Queue Empty\nExiting...")
#         popped = self.arr[self.start]
#         if self.currSize == 1:
#             self.start = -1
#             self.end = -1
#         else:
#             self.start = (self.start + 1) % self.maxSize
#         self.currSize -= 1
#         return popped


#     def top(self) -> int:
#         if self.start == -1:
#             print("Queue is Empty")
#             exit(1)
#         return self.arr[self.start]


#     def size(self) -> int:
#         return self.currSize