
# Learning the basic principles of algorithms using Python
## Source:
- **Grokking Algorithm** by Aditya Bharga [GitHub](https://github.com/egonSchiele/grokking_algorithms)

## Algorithms

Big O notation is the measure to see how an algorithm perform according to differents input dimension

### Binary Search
- Getting the result by dividing a dataset in 2 equal portions each time. It is more efficient than simple search and the worst case scenario can be calculated throw $log{_2}{n}={x}$ where n is the number of elements in the sorted list, while x represents the maximum's attempts. The big O notation here is $O(log{_2}{n})$

### Selection Sort
- Sorting the element of a list: it is quite expensive since it takes O(n^2) to complete the action

### Recursive
- An approach where a function calls itself. In order to avoid infinite loop, it's always made up by 2 parts:
  - base case --> when the function doesn't call itself again
  - recursive case
   
An example with factorial:

`def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)`