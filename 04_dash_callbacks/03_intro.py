from datetime import datetime

print(datetime.now())
print(datetime.now().hour)

def dekorator(func):
    def wrapper():
        if datetime.now().hour <= 17:
            func()
        else:
            pass
    return wrapper

@dekorator
def pora_dnia():
    print('Pora dnia')
    print('Godziny robocze')

pora_dnia()