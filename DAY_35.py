# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ---------------------------------------------------------INTRODUCTION TO LINKED LISTS--------------------------------------------------------
#problem-1

# Do not change code above.
# def constructLL(arr: [int]) -> Node:
#     # Write your code here
#     head = Node(arr[0])
#     prev = head
#     for i in range(1,len(arr)):
#         temp = Node(arr[i])
#         prev.next = temp
#         prev = temp
#     return head

# problem-2

# def insertAtFirst(list: Node, newValue: int) -> Node:
#     # Write your code here
#     newhead = Node(newValue,list)
#     return newhead

#problem-3

# def deleteLast(list: Node) -> Node:
#     # Write your code here
#     temp = list
#     while temp.next.next != None:
#         temp = temp.next
#     temp.next = None
#     return list

# problem-4

# def length(head) :
#     #Your code goes here
#     cnt = 0
#     while head != None:
#         head = head.next
#         cnt += 1

#     return cnt

#problemm-5

# def searchInLinkedList(head, k):
#     # Your code goes here.
#     temp = head
#     while temp != None:
#         if temp.data == k:
#             return 1
#         temp = temp.next
#     return 0