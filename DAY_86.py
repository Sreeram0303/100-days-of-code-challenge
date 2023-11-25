problem-1
def canSheMakeEqual(x: int, y: int) -> int:
    # Write your code here.
    X = min(x,y)
    Y = max(x,y)
    while X < Y:
        X += 1
        Y -= 2
    return int(X == Y)