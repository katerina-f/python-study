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
    i = 0
    user_input = ""
    people = {}
    while i < len(documents) or user_input == "q":
        user_input = input("Введите номер документа или q, чтобы выйти")
        if user_input == "q":
            print("Bye!")
            break
        for i, people in enumerate (documents):
            if user_input == people["number"]:
                print(people["name"])

p = get_name_from_document_number()
