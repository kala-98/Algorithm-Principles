

def binary_search(list, item):
    low, high = 0, len(list) - 1

    while low <= high:
        mid = (low + high) // 2 # searching for middle value (it's gonna round down the number if not even)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None

myList = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(myList, 5))
        