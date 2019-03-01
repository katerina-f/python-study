men_list = [
    {"name" : "John Smith", "age" : "23"},
    {"name" : "Jack Miller", "age" : "15"},
    {"name" : "Sam Goldberg", "age" : "19"},
    {"name" : "Bob Stone", "age" : "30"}
    ]

alphabet = {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9,
    "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26, " ": 0
}

def add_document():
    user_input = ""
    man = {}
    while user_input is not "q":
        if user_input.lower() == "q":
            break
        else:
            user_input = input('Введите имя или q, чтобы закончить')
            if user_input is not "q":
                man["name"] = user_input
        if user_input.lower() == "q":
            break
        else:
            user_input = input('Введите возраст или q, чтобы закончить')
            man["age"] = user_input
            men_list.append(man)
            return

def sexy_rating():
    names = []
    i = 0
    sum_list = []
    ages = []
    rat = []
    rating = []
    while i < len(men_list):
        for man in men_list:
            letters = list(man["name"])
            names.append(letters)
            i += 1
            age = int(man["age"])
            ages.append(age)
    for letters in names:
        sum_names = 0
        for letter in letters:
            letter = letter.lower()
            l = alphabet[letter]
            sum_names += l
        sum_list.append(sum_names)
    i = 0
    while i < len(sum_list):
        raty = ages[i] + sum_list[i]
        rat.append(raty)
        i += 1
    i = 0
    while len(rating) < len(rat):
        for man in men_list:
            r = "{} - {}".format(rat[i],man["name"])
            rating.append(r)
            i += 1
        rating.sort()
        print(rating)

def start_program():
    user_input = ""
    while user_input is not 'q':
        user_input = input('Выберите интересующий вас запрос : a - добавить имя в список, p - посмотреть рейтинг. Введите q для выхода.')
        if user_input == "a":
            add_document()
            for man in men_list:
                print(" {} - {}.".format(man["name"], man["age"]))
        elif user_input == "p":
            sexy_rating()
        elif user_input == "q":
            print("До свидания!")
start_program()
