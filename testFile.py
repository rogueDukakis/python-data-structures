
# Question regarding lists 
# Question 1: Scale a list based on the elements
input_list = [2,3,-4,5,6,0]
output_list_scale = []

def scale_list_by_K():
    # Create another lsit to return

    for i in input_list:
        if i > 0:
            for j in range(i): # Going from 0 to i for every element
                output_list_scale.append(i)
            
    return output_list_scale
print(scale_list_by_K())


