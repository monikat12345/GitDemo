from oopsDemo import Calculator


class Child_c(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self, 7, 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.addition()

chobj = Child_c()
print(chobj.get_complete_data())

