class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def f_name(self):
        print("Меня зовут", self.first_name)

    def l_name(self):
        print("Моя фамилия -", self.last_name)

    def fl_name(self):
        print("Я -", self.first_name, self.last_name)
