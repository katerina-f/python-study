documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name_from_document_number():
    user_input = ""
    while  user_input is not "q":
        user_input = input("Введите номер документа или q, чтобы выйти.")
        if user_input == "q":
            break
        for people in documents:
            if user_input == people["number"]:
                print(people["name"])
                return
        print("Документ не найден")

def get_documents_list():
    i = 0
    user_input = ""
    while i < len(documents):
        user_input = input("Введите 'print', чтобы напечатать список документов")
        for i, people in enumerate(documents):
            if user_input == "print":
                i += 1
            print(people["type"],people["number"],people["name"])

def get_shelf_number():
    user_input = ""
    while user_input is not "q":
        user_input = input("Введите номер документа или q, чтобы выйти.")
        for number, shelf in directories.items():
            if user_input in shelf:
                print("Документ находится на полке номер {}".format(number))
                return
        print('Документ не найден')

def add_document():
    user_input = ""
    man = {}
    while user_input is not "q":
        if user_input.lower() == "q":
            break
        else:
            user_input = input('Введите тип документа или q, чтобы закончить')
            man["type"] = user_input
        if user_input.lower() == "q":
            break
        else:
            user_input = input('Введите номер документа или q, чтобы закончить')
            man["number"] = user_input
        if user_input.lower() == "q":
            break
        else:
            user_input = input('Введите имя и фамилию владельца или q, чтобы закончить')
            man["name"] = user_input
            documents.append(man)
        if user_input.lower() == "q":
            break
        else:
            user_input = input("Введите номер полки для документа или q, чтобы закончить")
            if user_input in directories:
                directories[user_input].append(man["number"])
            else:
                directories[user_input] = [man["number"]]
            return

def data_base() :
    user_input = ""
    while user_input is not 'q':
        user_input = ""
        user_input = input('Выберите интересующий вас запрос : p - поиск по документам, l - список документов, s - поиск местоположения документа, a - добавить документ. Введите q для выхода.')
        if user_input == "p":
            get_name_from_document_number()
        elif user_input == "l":
            get_documents_list()
        elif user_input == "s":
            get_shelf_number()
        elif user_input == "a":
            add_document()
        elif user_input == "q":
            print("До свидания!")

data_base()
