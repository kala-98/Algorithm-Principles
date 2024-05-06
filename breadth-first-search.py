
from collections import deque 
# this module provides the data type deque which is similar to list with some adding features

def person_is_seller(person):
    if person[0] == "M": # just for test
        return True

def find_mango_seller():
    graphs = {}
    graphs["you"] = ["Alice", "Cristina", "Francesca"]
    graphs["Alice"] = []
    graphs["Cristina"] = []
    graphs["Francesca"] = ["Maria"]
    graphs["Maria"] = []

    search_queue = deque()
    search_queue += graphs["you"]

    while search_queue: # until there's something here..
        person = search_queue.popleft() # takes the 1st element and remove it
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return True 
        else:
            search_queue += graphs[person]
    return False 

