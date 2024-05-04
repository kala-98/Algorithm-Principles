
# Divide and Conquer way of thinking: it encourages the use of recursive functions, reducing the problem size to the most basic/simple one
# In this case we are going to find the sum of an array, reducing the list until it gets just one element

def sum(arr):
    if len(arr) == 1: # base case
        return arr[0]
    else:             # recursive case
        return arr[0] + sum(arr[1::])
    
def count(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + count(arr[1::])
    
def max_value(arr, idx=0, max_val=None):
    if idx == len(arr):
        return max_val 
    
    if max_val is None or arr[idx] > max_val:
        max_val = arr[idx]  

    return max_value(arr, idx + 1, max_val) 

    
lista = [5, 3, 6, 13, 5]
    
print(f"The sum is: {sum(lista)}")    
print(f"The count is: {count(lista)}")
print(f"The max number is: {max_value(lista)}")