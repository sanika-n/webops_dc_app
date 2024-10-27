def flatten(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten(element))   
        else:
            flat_list.append(element)  
    return flat_list


nested_list = eval(input("enter a nested list"))
flat_list = flatten(nested_list)
print(flat_list)