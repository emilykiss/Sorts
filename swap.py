# swap = [1, 2, 'four', 3]

# # Swapping easily in python
# # Order things = New order of things
# swap[2], swap[3] = swap[3], swap[2]

# print(swap)

li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

# Check if a list is sorted
# def is_sorted(li):
#     for i in range(len(li) -1):
#         if li[i] > li[i + 1]:
#             return False
#         else:
#             return True

# print(is_sorted(li))

# Online example
def bubble_sort(li):
    for i in range(len(li)):
        sorted = False
        for j in range(0, len(li) - i -1):
            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp

    if not sorted:
        return

bubble_sort(li)
print(li)

# Weston's example
def sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True

def sort(li):
    # Tells us if the list is sorted
    swapped = True

    while swapped:
         # Assume that no swap will be made
        swapped = False
        for i in range(len(li) -1):
            # Check the neighbors values -- if current is greater than the one to the right, make the swap
            if li[i] > li[i + 1]:
                # Wrong order -- need to swap
                li[i], li[i + 1] = li[i + 1], li[i]
                swapped = True

sort(li)
print(li)