# def kDistinctChars(k, s):
#     n = len(s)
#     i = 0
#     j = 0
#     length = 0
#     char_count = {}

#     while j < n:
#         char_count[s[j]] = char_count.get(s[j], 0) + 1

#         while len(char_count) > k:
#             char_count[s[i]] -= 1
#             if char_count[s[i]] == 0:
#                 del char_count[s[i]]
#             i += 1

#         length = max(length, j - i + 1)
#         j += 1

#     return length
