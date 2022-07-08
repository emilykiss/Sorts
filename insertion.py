# This was so confusing for me- looked at https://www.programiz.com for help!!
def sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
                
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


data = [9, 4, 1, 3, 6]
sort(data)
print(data)

# In class example
li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]

def sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True

def insertion(li):
    # Iterate over the list, loop downward when we find a value that is smaller than what is to the left
    for index in range(len(li)):
        # We need to know the current number for comparisons
        current_num = li[index]
        # The position sliding back down the list
        comparison_position = index - 1 
        # If the comparison position is less than or equal to zero don't continue 
        while comparison_position >= 0 and current_num < li[comparison_position]:
            # Swap the values down while both conditions are met
            li[comparison_position], li[comparison_position + 1] = li[comparison_position + 1], li[comparison_position]
            comparison_position -= 1
    
insertion(li)
print(sorted(li))
print(li)