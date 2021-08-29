#FIRST QUESTION SOLUTION

def flatten_list(some_list):
    
    while True:
        flattened_list = []
            
        for element in some_list:
            if type(element) != list:
                flattened_list.append(element)
            else:
                for item in element:
                    flattened_list.append(item)
        some_list = flattened_list
        
        list_types = []
        for element in some_list:
            list_types.append(type(element))
        if list not in list_types:
            break

    return some_list
    
example_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(f"Example list:   {example_list}")
print(f"Flattened list: {flatten_list(example_list)}")



#SECOND QUESTION SOLUTION

def reverse_list(some_list):
    
    new_list = []
    
    for element in some_list[::-1]:
        if type(element) == list:
            new_list.append(element[::-1])
        else:
            new_list.append(element)
            
    return new_list
    
example_list = [[1, 2], [3, 4], [5, 6, 7]]

print(f"Example list: {example_list}")
print(f"Reversed list: {reverse_list(example_list)}")
