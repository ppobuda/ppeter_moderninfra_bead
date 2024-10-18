#Pálosi Péter - JCZ9BB
def linearSearch(myArray: list[int], num: int):
    #returns the index of the first occurence in the array of the input integer, returns -1 if the integer is not in the array
    i = 0
    while i < len(myArray):
        if num == myArray[i]:
            return i
        i = i + 1
    return -1
        

    
    

    

