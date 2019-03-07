
def sum(arr):
    if arr != []:
        result = arr.pop(0) + sum(arr)
        return result
    elif arr == []:
        return 0
print(sum(arr))
