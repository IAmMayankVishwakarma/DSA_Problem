arr = [3,0,4,1,5,9,-1,6,5,3,5]
# findlowest number in the array
def findLowest(arr):
    lowest = arr[0]
    for i in arr:
        if i < lowest:
            lowest = i
    return lowest
print(findLowest(arr)) # 1
# find the lowest number in the array using recursion           
