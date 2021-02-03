class Animal(object):
    name = ''
    age = 0

    def make_sound(self):
        print('Some weird sound!!!!!!!')

class Cat(Animal):

    def make_sound(self):
        print('Miaaaaau!!!')


class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print('Guaaaau!!!!')


pastor_aleman = Dog()
pelusa = Cat()

pelusa.make_sound()
pastor_aleman.make_sound()

### DECORATORS ###
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def print_args(*args, **kwargs):
    print(args, kwargs)


print_args(3, 2, age=13)
