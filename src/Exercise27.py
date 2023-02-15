import array as arr
import random
def function_with_arrays(array1):
    sarray = arr.array("i", [])
    array2 = arr.array("i",[])
    for values in range(-len(array1), 2 * len(array1)):
        sarray.append(values)
    for values in sarray:
        if values not in array1:
            array2.append(values)
    return array2
anwer = function_with_arrays((arr.array("i", [1,2,3,4,5])))
print(anwer

#i used a list to get all numbers between the negative lengh of array and 2 * the lenth of array
#with that, i checked and gave back all other values except those that in the actual array using loops