

class Animal(object):
    age = 0
    name = ''


class Dog(Animal):
    pass


lucas = Dog()
# print(lucas.age)

### DECORATORS

def do_something(func):
    def wrapper(*args, **kwargs):
        print('User is not authenticated!!')
        func(*args, **kwargs)
        print('User is authenticated!!')
    return wrapper


@do_something
def say_hello(name, *args, **kwargs):
    print(args, kwargs)
    print('Hola ' + name)

say_hello('Raul', 'ISC', lastname='Novelo', age=21)
