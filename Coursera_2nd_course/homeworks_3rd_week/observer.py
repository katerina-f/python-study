from abc import abstractmethod, ABC

class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        if not message["title"] in self.achievements:
            self.achievements.add(message["title"])



class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if not message in self.achievements:
            self.achievements.append(message)


engine = ObservableEngine()
full_print = FullNotificationPrinter()
short_print = ShortNotificationPrinter()
full_print1 = FullNotificationPrinter()

engine.subscribe(full_print)
engine.subscribe(short_print)
engine.subscribe(full_print1)


engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
engine.notify({"title": "Молодец", "text": "Всех убил"})
engine.notify({"title": "Красавчик", "text": "Дается при выполнении всех заданий в игре"})

print(engine.subscribers)
print(full_print.achievements)
print(short_print.achievements)

engine.unsubscribe(full_print)
print(engine.subscribers)
