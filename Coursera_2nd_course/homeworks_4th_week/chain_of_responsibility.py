class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type):
        self.type = type


class EventSet:
    def __init__(self, value):
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and isinstance(event.value, int):
            obj.integer_field = event.value
            return obj.integer_field
        elif isinstance(event, EventGet) and event.type is int:
            return obj.integer_field
        else:
            return super().handle(obj,event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and isinstance(event.value, float):
            obj.float_field = event.value
            return obj.float_field
        elif isinstance(event, EventGet) and event.type is float:
            return obj.float_field
        else:
            return super().handle(obj,event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventSet) and isinstance(event.value, str):
            obj.string_field = event.value
            return obj.string_field
        elif isinstance(event, EventGet) and event.type is str:
            return obj.string_field
        else:
            return super().handle(obj,event)


obj = SomeObject()

chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

chain.handle(obj, EventSet(1))
chain.handle(obj, EventSet(1.1))
chain.handle(obj, EventSet("str"))

chain.handle(obj, EventGet(int))
chain.handle(obj, EventGet(float))
chain.handle(obj, EventGet(str))
