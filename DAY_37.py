# -----------------------------------------
# problem-1

# def findMiddle(head):
#     temp1 = head
#     temp2 = head
#     while temp2 != None and temp2.next != None:
#         temp1 = temp1.next
#         temp2 = temp2.next.next
#     return temp1

# -------------------------------------------
#problem-2
# def reverseLinkedList(head):
#     if not head:
#         return None
#     if head.next == None:
#         return head
#     temp = head
#     prevNode = None
#     while temp != None:
#         nextnode = temp.next
#         temp.next = prevNode
#         prevNode = temp
#         temp = nextnode
#     head = prevNode
#     return head

# ----------------------------------------------
# problem-3

# def detectCycle(self, head: Optional[ListNode]) -> bool:
#         slow_pointer = head
#         fast_pointer = head
#         while fast_pointer and fast_pointer.next:
#             slow_pointer = slow_pointer.next
#             fast_pointer = fast_pointer.next.next
#             if slow_pointer == fast_pointer:
#                 return True
#         return False

# ----------------------------------------------------
# problem - 4
# def firstNode(head):
#     # Write your code here
#     if head == None or head.next == None:
#         return None
#     slow_pointer = head
#     fast_pointer = head
#     while fast_pointer.next != None and fast_pointer.next.next != None :
#         slow_pointer = slow_pointer.next
#         fast_pointer = fast_pointer.next.next
#         if slow_pointer == fast_pointer:
#             slow_pointer = head
#             while slow_pointer != fast_pointer:
#                 slow_pointer = slow_pointer.next
#                 fast_pointer = fast_pointer.next
#             return slow_pointer
#     return None

# ----------------------------------------------------
# problem-5
# def lengthOfLoop(head):
#     if head is None or head.next is None:
#         return 0  # No loop or a single-node list has a loop of length 1

#     slow = head
#     fast = head
#     loop_detected = False
#     length = 0

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         length += 1

#         if slow == fast:
#             loop_detected = True
#             break

#     if not loop_detected:
#         return 0  # No loop detected

#     # Now, one of the pointers is at the meeting point. Keep one pointer at the
#     # meeting point and move the other pointer until they meet again.
#     meeting_node = slow
#     length_of_loop = 1  # Start counting from the meeting point

#     while slow.next != meeting_node:
#         slow = slow.next
#         length_of_loop += 1

#     return length_of_loop

# ---------------------------------------
# problem-6

# def deleteMiddle(head):
#     # Write your code here.
#     if not head or not head.next:
#         return None
#     slow = head
#     fast = head
#     prev = None
#     while fast != None and fast.next != None:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next
#     prev.next = slow.next
#     return head