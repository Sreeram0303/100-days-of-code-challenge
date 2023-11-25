from typing import Tuple

def minSubstring(a, b):
    mpp = {}  # Dictionary to store character frequencies in string b
    for char in b:
        if char in mpp:
            mpp[char] += 1
        else:
            mpp[char] = 1

    l = 0
    r = 0
    start = -1
    count = len(mpp)
    len_ = float('inf')

    while r < len(a):
        if a[r] in mpp:
            mpp[a[r]] -= 1
            if mpp[a[r]] == 0:
                count -= 1

        if count == 0:
            while count == 0:
                if a[l] in mpp:
                    mpp[a[l]] += 1
                    if mpp[a[l]] == 1:
                        count += 1
                        if r - l + 1 < len_:
                            len_ = r - l + 1
                            start = l
                l += 1

        r += 1

    if start == -1:
        return ""

    return a[start:start + len_]

