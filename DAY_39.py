# ---------------------------------------
# problem-1

# def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
        
#         o,e,heade = head, head.next,head.next        
    
#         while e and e.next:
#             o.next = o.next.next
#             e.next = e.next.next
#             o = o.next
#             e = e.next  
        
#         o.next = heade

#         return head    

# --------------------------------------------
# problem-2

# def segregateEvenOdd(head):
#     even_head = None
#     even_tail = None
#     odd_head = None
#     odd_tail = None
#     current = head
#     while current is not None:
#         if current.data % 2 == 0:  
#             if even_head is None:
#                 even_head = even_tail = current
#             else:
#                 even_tail.next = current
#                 even_tail = even_tail.next
#         else:  
#             if odd_head is None:
#                 odd_head = odd_tail = current
#             else:
#                 odd_tail.next = current
#                 odd_tail = odd_tail.next
#         current = current.next
#     if even_tail:
#         even_tail.next = odd_head
#     else:
#         even_head = odd_head
#     if odd_tail:
#         odd_tail.next = None
#     return even_head