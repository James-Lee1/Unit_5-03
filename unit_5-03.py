# Created by : James Lee
# Created on : 13 Nov. 2017
# Created for : ICS3UR
# This program show the smallest value in an array

def find_lowest_value(arrays = []):
    # Finds lowest value in an array

    value_number_in_array = 0

    for value in arrays:
        if value_number_in_array == 0:
           value_number_in_array = value
        else:
             if value_number_in_array > value:
                value_number_in_array = value
             else: 
             	  value_number_in_array = value_number_in_array
                            
    return value_number_in_array                                 


array = [9,13,29,83,10,29]
find_lowest_value(array)

smallest_value = find_lowest_value(array)
print("The minimum value of the array is: " + str(smallest_value))
