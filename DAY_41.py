# --------------------------------------
# problem-1

# def deleteAllOccurrences(head: Node, k: int) -> Node:---------------solution i thought
#     # Write your code here
#     if not head:
#         return None 
#     prevNode = None
#     nextNode = None
#     current = head
#     while current.next:
#         if current.data == k and current != head:
#             current.next.prev = current.prev
#             current.prev.next = current.next
#         elif current.data == k:
#             head = current.next
#             current.next.prev = None
#         current = current.next
#     if current.data == k and current != head:
#         current.prev.next = None
#     elif current.data == k and current == head:      
#         return None
#     return head



# def deleteAllOccurrences(head: Node, k: int) -> Node:--------easy soln
#     # Handle the case where the linked list is empty
#     if not head:
#         return None
    
#     temp = head
#     while temp:
#         if temp.data == k:
#             if temp.prev:
#                 temp.prev.next = temp.next
#             if temp.next:
#                 temp.next.prev = temp.prev
#             if temp  == head:
#                 head = head.next
#             temp = temp.next
#         else:
#             temp = temp.next
#     return head

# ---------------------------------------------------
# problem-2:

# def findPairs(head: Node, k: int) -> [[int]]:
#     start = head
#     end = head
#     ans = []
#     # Traverse the linked list to the end.
#     while end.next != None:
#         end = end.next
#     while start.data < end.data:
#         sum = start.data + end.data
#         if sum == k:
#             ans.append([start.data, end.data])
#         if sum < k:
#             start = start.next
#         else:
#             end = end.prev

# --------------------------------------------------------
#problem-3

# def removeDuplicates(head: Node) -> Node:
#     # Write your code here
#     temp = head
#     temp2 = head
#     while temp.next:
#         if temp.data != temp.next.data:
#             temp2.next = temp.next
#             temp2 = temp2.next
#         temp = temp.next
#     temp2.next = None
    # return head