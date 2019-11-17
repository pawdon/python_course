my_list = []  # pusta lista
my_list = list()  # pusta lista
my_list = ['Jan', 'Adam', 'Kamil']  # lista z elementami
name = my_list[0]  # Jan
name = my_list[1]  # Adam
# for x in my_list:  # w pierwszej iteracji x = 'Jan'

my_dict = {}  # pusty slownik
my_dict = dict()  # pusty slownik
my_dict = dict(name='Jan', age=16)  # slownik z elementami
my_dict = {3: 'Jan', (2, 3): 16, 'x': 87}  # slownik z elementami
my_dict = {'name': 'Jan', 'age': 16}  # slownik z elementami
# kluczem powinno byc cokolwiek immutable
name = my_dict['name']  # Jan
name = my_dict.get('name')  # Jan
name = my_dict.get('name', 'DEFAULT')  # Jan
# height = my_dict['height']  # wyjatek!!!
height = my_dict.get('height', 100)  # OK
keys = my_dict.keys()  # ['name', 'age']
values = my_dict.values()  # ['Jan', 16]
# for x in my_dict:  # iterowanie po kluczach, wiec w pierwszej iteracji x == 'name'
# for key, value in my_dict.items():  # w pierwszej iteracji key = 'name', value = 'Jan'

"""
# one liners
x = wartosc_jesli_warunek_spelniony if warunek else wartosc_jesli_nie_spelniony
# <==>
if warunek:
    x = wartosc_jesli_warunek_spelniony
else:
    x = wartosc_jesli_nie_spelniony
    

# fun(value) - dowolna funkcja ktora zwraca cokolwiek
x = [fun(value) for value in list if warunek]
# <==>

x = []
for value in list:
    if warunek:
        x.append(fun(value))
        
x = {fun1(key): fun2(value) for key, value in costam if warunek}
x = {}
for key, value in costam:
    if warunek:
        x[fun1(key)] = fun2(value)

"""


"""
WRAPPERS

@wrapper
def my_fun...

<==> my_fun = wrapper(my_fun)

@wrapper
class MyClass...

<==> MyClass = wrapper(MyClass)

"""
