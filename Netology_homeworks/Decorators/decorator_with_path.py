from datetime import datetime


def get_loggs_with_path(path):
    def get_loggs(func):
        def wrapped(*args,**kwargs):
            time = datetime.now()
            result = func(*args,**kwargs)
            name = func.__name__
            params = f'Args:{args} Kwargs{kwargs}'
            logg = f'{time} Name: {name}, Result: {result}, {params}.\n'
            try:
                with open(path, 'a') as f:
                        f.write(logg)
            except FileNotFoundError:
                with open(path, 'w') as f:
                        f.write(logg)
            return result
        return wrapped
    return get_loggs


@get_loggs_with_path('loggs 2.txt')
def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]

        if guess == item:
            return list[mid]

        elif guess > item:
            high = mid - 1

        else:
            low = mid + 1
    return None


my_list = [11,43,20,7,29]
print(binary_search(my_list, 20))

my_list = [1,3,5,7,9]
print(binary_search(my_list, 3))

my_list = [11,43,20,7,29]
print(binary_search(my_list, 2))

my_list = [11,43, 1, 56, 34]
print(binary_search(my_list, 1))
