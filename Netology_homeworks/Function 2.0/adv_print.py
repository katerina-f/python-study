import textwrap

def adv_print(*args, **kwargs):
    start = ''
    in_file = False

    try:
        start = kwargs['start']
    except KeyError:
        start = '\n'

    try:
        max_line = kwargs['max_line']
    except KeyError:
        max_line = 72


    try:
        for arg in args:
            start += str(arg)
    except IndexError:
        pass

    text = ''
    text = textwrap.fill(start, width=max_line)

    try:
        in_file = kwargs['in_file']
        if in_file is False:
            pass
        try:
            with open('file.txt', 'r+') as f:
                f.write(text)
        except FileNotFoundError:
            with open('file.txt', 'w') as f:
                f.write(text)
    except KeyError:
        pass

    print(text)



adv_print('Продвинутый print (необязательное задание) Разработать свою реализацию функции print - adv_print. Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:', start='текст:\n', in_file = True, max_line=50)
