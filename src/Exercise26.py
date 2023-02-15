import array as arr
def function_with_arrays(array1, array2):
    array3 = arr.array("i", [])
    for values in array1:
        if values not in array2:
            array3.append(values)
    return array3

answer = function_with_arrays((arr.array("i", [1,2,3,8,5])), (arr.array("i", [6,7,8,9,10])))
print(answer)

#notice that i used this loops to loop through and checked values, then in the test, i reapeated 8 in both arrays and it was not printed, so it makes sense