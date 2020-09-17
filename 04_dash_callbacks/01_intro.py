def dekorator(func):
    return func

def hello_world():
    print('Hello world')

hello_world_dekorator = dekorator(hello_world)

@dekorator
def hello_world_2();
    print('hello world')

