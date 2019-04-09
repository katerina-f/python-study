
def main():
    men_list = [
        {"name" : "John Smith", "age" : "23"},
        {"name" : "Jack Miller", "age" : "15"},
        {"name" : "Sam Goldberg", "age" : "19"},
        {"name" : "Bob Stone", "age" : "30"}
        ]

    alphabet = {
        "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8,
        "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15,
        "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22,
        "w" : 23, "x" : 24, "y" : 25, "z" : 26, " ": 0
        }

    user_input = ""
    while user_input is not 'q':
        user_input = input('Выберите интересующий вас запрос :a - добавить имя в список, p - посмотреть рейтинг. Введите q для выхода.\n')
        if user_input == "a":
            add_document(men_list, alphabet)
        elif user_input == "p":
            get_sexy_rating(men_list, alphabet)
        elif user_input == "q":
            print("До свидания!")


def add_name(alphabet):
    name = input('Введите имя или q, чтобы закончить\n')
    for letter in list(name):
        if letter.lower() in alphabet.keys():
            continue
        else:
            print("Введите имя используя буквы\n")
            return add_name(alphabet)
    return name


def add_age():
    age = input('Введите возраст или q, чтобы закончить\n')
    try:
        age = int(age)
        return age
    except ValueError:
        print("Введите возраст используя цифры\n")
        return add_age()


def add_document(men_list, alphabet):
    men_list.append({"name": add_name(alphabet), "age": add_age()})
    for man in men_list:
        print("{} - {}.".format(man["name"], man["age"]))


def get_sum_name(man, alphabet):
    letters = list(man["name"])
    value = 0
    for letter in letters:
        letter = alphabet[letter.lower()]
        value += letter
    return value


def get_man_rating(man, alphabet):
    man_rating = int(man["age"]) + get_sum_name(man, alphabet)
    return man_rating


def get_rating_dict(men_list, alphabet):
    rating_dict = {}
    for man in men_list:
        man_rating = get_man_rating(man, alphabet)
        if man_rating in rating_dict:
            rating_dict[man_rating] += f", {man['name']}"
        else:
            rating_dict[man_rating] = f"{man['name']}"
    return rating_dict


def get_sexy_rating(men_list, alphabet):
    rating = [f"{key} - {value}" for key, value in get_rating_dict(men_list, alphabet).items()]
    rating.sort()
    print(rating)


if __name__ == "__main__":
    main()
