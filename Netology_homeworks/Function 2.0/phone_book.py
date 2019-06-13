
class Contact:
    def __init__(self, name, surname, number, elected=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.elected = elected
        self.info = kwargs


    def __str__(self):
        info = ''
        for key, value in self.info.items():
            info += f'    {key}: {value}\n'
        if self.elected is True:
            contact_card = f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.number}\nВ избранных: да\nДополнительная информация:\n{info}'
        else:
            contact_card = f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.number}\nВ избранных: нет\nДополнительная информация:\n{info}'
        return contact_card


class PhoneBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.phone_book = []


    def add_contact(self, contact):
        self.phone_book.append(contact)
        print(f'Контакт {contact.name} {contact.surname} добавлен в {self.book_name}')


    def del_with_number(self, number):
        for contact in self.phone_book:
            if number == contact.number:
                self.phone_book.remove(contact)
                print(f'Контакт {contact.name} {contact.surname} удален')
                return
            else:
                print('Номер не найден')


    def get_all_contacts(self):
        print('Все контакты','\n')
        for contact in self.phone_book:
            print(contact)


    def get_elected(self):
        print('Избранные контакты', '\n')
        for contact in self.phone_book:
            if contact.elected is True:
                print(contact)


    def get_with_name(self, name, surname):
        for contact in self.phone_book:
            if name == contact.name and surname == contact.surname:
                print('Карточка контакта: ', '\n')
                print(contact)
                return
            else:
                print('Контакт не найден')


# jhon = Contact('Jhon', 'Smith', '+71234567809', True, telegram='@jhony', email='jhony@smith.com')
#
# simona = Contact('Simona', 'Smith', '+71234569987', True, telegram='@simona', email='simona@smith.com')
#
# ramen = Contact('Simona', 'Ramen', '+71234569666', telegram='@simona', email='simona@ramen.com')
#
# book = PhoneBook('MyContacts')

# book.add_contact(jhon)
# book.add_contact(simona)
# book.add_contact(ramen)
# book.get_all_contacts()
# book.del_with_number('+71234567809')
# book.get_elected()
# book.get_with_name('Simona', 'Smith')
