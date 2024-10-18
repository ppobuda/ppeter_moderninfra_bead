def replaceNum(myArray: list[int], idx: int, num: int):
    #replaces the number in array in the given index (first param) to the given number (second param)
    #if the idx is out of bounds of the array, the function leaves the array as it is   
    if idx >= 0 and idx < len(myArray):
        myArray[idx] = num
        return myArray
    return myArray
    