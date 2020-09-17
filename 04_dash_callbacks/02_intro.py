def dekorator(func):
    def wrapper():
        func()
        print('Wywolanie funkckji wrapper')
    return wrapper

@dekorator
def func_2():
    print('wywołanie func_2')

func_2()