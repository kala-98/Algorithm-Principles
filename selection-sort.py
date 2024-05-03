
# finding the smallest item in an array
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index 
    

# selection sort algorithm
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) # removing the selected index and insert the item into new array
    return newArr

lista = [5, 4, 2, 10, 432, 1, 14]
print(selectionSort(lista))