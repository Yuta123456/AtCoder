def binary_search(left, right):
    if right - left <= 1:
        return right
    middle = (right + left)//2
    if is_can(middle):
        return binary_search(middle, right)
    else:
        return binary_search(left, middle)