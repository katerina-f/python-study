import re
import csv

def main():
    contacts_list = get_raw_list('phone_book.csv')
    for contact in contacts_list:
        if len(contact) > 7:
            contact.pop(-1)
        contact = get_pretty_contact(contact)

    new_list = get_new_contact_list(contacts_list)

    write_new_list('new_phonebook.csv', new_list)


def get_raw_list(file):
    with open(file) as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
      return contacts_list


def get_pretty_contact(contact):
    fio = [contact[0], contact[1], contact[2]]
    number = contact[5]
    fio = formating_rows(get_pretty_names(fio))[:3]
    number = get_pretty_phones(number)
    contact[0], contact[1], contact[2], contact[5]= fio[0], fio[1], fio[2], number
    return contact


def formating_rows(data):
    data = data.replace("'", "",)
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(',')
    return data


def get_pretty_names(fio):
    for_name = "[\s']?([А-Я][а-я]+)[\s',]+([А-Я][а-я]+)[\s']?[\s',]+([А-Я][а-я]+)?[\s']?"
    fio = re.sub(for_name, r"'\1', '\2', '\3'", str(fio))
    return fio


def get_pretty_phones(number):
    for_phone = '((\+7|8)\s?\(?(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{2})[\s\-]?(\d{2})\s?\(?(доб\.\s?\d+)?\)?)'
    try:
        number = re.sub(for_phone, r'+7(\3)\4-\5-\6 \7', number)
    except TypeError:
        number = ''
    return number


def get_new_contact_list(contacts_list):
    new_list = [['lastname', ' firstname', ' surname', 'organization', 'position', 'phone', 'email']]
    list_1 = contacts_list
    for contact in list_1[1:]:
        for i in contacts_list[1:]:
            if i[0] == contact[0]:
                for x in range(7):
                    if i[x] == '' or ' ' and contact[x] != '':
                        i[x] = contact[x]

    for contact in contacts_list:
        if contact not in new_list:
            new_list.append(contact)

    return new_list


def write_new_list(file, list):
    with open(file, "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(list)


if __name__ == '__main__':
    main()
