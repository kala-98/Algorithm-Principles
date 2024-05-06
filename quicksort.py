import random 

def quicksort(arr):
    
    if len(arr) < 2: # in case of 0/1 element it's already sorted
        return arr 
    else:
        random_int = random.randint(0, len(arr) - 1)
        pivot = arr[random_int] # getting a random element from the array

        less = [i for i in arr if i < pivot]
        more = [i for i in arr if i > pivot]

        return quicksort(less) + [pivot] + quicksort(more)
    
lista = [5, 8, 2, 15, 9, 6]
print(quicksort(lista))
