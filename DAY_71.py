# ----------------------------------
# problem -1 
# Infix to postfix

# def infixToPostfix(s):
#     def prec(c):
#         if c == '^':
#             return 3
#         elif c == '/' or c == '*':
#             return 2
#         elif c == '+' or c == '-':
#             return 1
#         else:
#             return -1
#     stack = []  # For stack operations
#     result = ""

#     for i in range(len(s)):
#         c = s[i]

#         # If the scanned character is an operand, add it to the output string.
#         if c.isalnum() or c.isdigit():
#             result += c

#         # If the scanned character is '(', push it to the stack.
#         elif c == '(':
#             stack.append('(')

#         # If the scanned character is ')', pop from the stack and add to the output string until '(' is encountered.
#         elif c == ')':
#             while stack and stack[-1] != '(':
#                 result += stack.pop()
#             stack.pop()  # Pop '('

#         # If an operator is scanned
#         else:
#             while stack and prec(s[i]) <= prec(stack[-1]):
#                 result += stack.pop()
#             stack.append(c)

#     # Pop all the remaining elements from the stack
#     while stack:
#         result += stack.pop()

#     return result

# -----------------------------------------
# prefix to infix

# def prefixToInfixConversion(prefix):
# 	def isOperator(c):
# 	    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
# 	    	return True
# 	    else:
# 	    	return False
# 	stack = []
	
# 	# read prefix in reverse order
# 	i = len(prefix) - 1
# 	while i >= 0:
# 		if not isOperator(prefix[i]):
			
# 			# symbol is operand
# 			stack.append(prefix[i])
# 			i -= 1
# 		else:
		
# 			# symbol is operator
# 			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
# 			stack.append(str)
# 			i -= 1
	
# 	return stack.pop()



