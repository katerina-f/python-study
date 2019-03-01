man = 9
petrovich = 10
serega = 5
rest = 5
tree = man + petrovich + serega + rest
work_end = 480
number = 0
user_input = ""

while user_input is not "q":
    time_spent = 0
    user_input = input("Петрович сегодня болеет? 1 если да, 0 если нет. Для выхода нажмите q")
    if user_input.lower() == "q":
        print("Вы закончили")
        break

    try:
        petrovich_condition = int(user_input)
    except:
        print("Что-то пошло не так, повторите ввод еще раз")
        continue

    if  petrovich_condition == 1:
        while time_spent <= work_end:
         time_spent += tree
         number = 0
        print("Рабочий день закончен, посажено {} деревьев.".format(number))

    elif petrovich_condition == 0:
        while time_spent <= work_end:
         time_spent += tree
         number += 1
        print("Рабочий день закончен, посажено {} деревьев.".format(number))
