import hashlib
import json
import wikipedia


WIKI_LINKS = 'wiki_links.txt'
COUNTRIES = 'countries.json'


def main():
    iter = WikiIter(COUNTRIES)
    while True:
        next(iter)

    g = get_hash(WIKI_LINKS)
    while True:
        print(next(g))


# iterator
class WikiIter():

    def __get_data(self):
        if not self.file:
            return {}

        with open(self.file, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return json.loads(raw_data)
            return {}


    def __get_country(self):
        country = self.data[self.index]['name']['common']
        return country


    def __get_link(self):
        page = wikipedia.page(self.__get_country())
        link = page.url
        return link


    def __init__(self, file = ''):
        self.file = file
        self.data = self.__get_data()
        self.index = 0


    def __iter__(self):
        return self.data


    def __next__(self):
        try:
            data = f'{self.__get_country()} : {self.__get_link()}\n'
            with open(WIKI_LINKS, 'r+') as f:
                if self.__get_country() in f.read():
                    pass
                else:
                    f.write(data)
        except FileNotFoundError:
            with open(WIKI_LINKS, 'w') as f:
                f.write(data)
        except StopIteration as ex:
            print('StopIteration')
        self.index += 1


#generator
def get_hash(path):
    for line in path:
        line = line.encode()
        yield hashlib.md5(line).hexdigest()


if __name__ == '__main__':
    main()
