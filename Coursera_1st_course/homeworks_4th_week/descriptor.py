class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value

    def __get__(self, obj, obj_type):
        return self.value-(self.value * obj.commission)

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

#new_account = Account(0.1)
#new_account.amount = 100

#print(new_account.amount)
