# getter & setter
class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(self._value)

    @property
    def new_value(self):
        return  10*self._value

    @new_value.setter
    def new_value(self, new_val):
        self._value = new_val/10

x = MyClass(11)
x.new_value = 400
print(x.new_value)
x.show()
