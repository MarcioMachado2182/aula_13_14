class Parent1():

    def show(self):
        print('Inside Parente1')

class Parent2():
    def display(self):
        print('Inside Parente2')

class Child(Parent1, Parent2):
    def show(self):
        print('Inside child')


obj = Child()
obj.show()
obj.display()