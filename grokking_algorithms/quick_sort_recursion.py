def quicksort(array):

    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([18, 23, 1, 4, 2, 34, 14, 10, 5, 7]))


A = [5,2,4,6,1,3,2,6]

def merge(a, p, q, r):
    print(a)
    print(p)
    print(q)
    print(r)

def sort(a, p, r):
    if p < r:

        q = round((p+r)/2)
        sort(a, p, q)
        sort(a, q+1, r)
        return merge(a, p, q, r)
    else:
        return a



sort(A, 1, len(A))
