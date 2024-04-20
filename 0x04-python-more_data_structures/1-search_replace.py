#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = []
    
    for item in my_list:
        if item == search:
            newl.append(replace)
        else:
            newl.append(item)
    
    return (newl)
