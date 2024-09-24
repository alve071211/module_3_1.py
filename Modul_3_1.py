calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    return a, b, c

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Доброе утро'))

def is_contains(string,list_to_search):
    count_calls()
    a = string.lower()
    b = [s.lower() for s in list_to_search]
    return a in b

print(is_contains('Urban', ['ban', 'BaNaN','urBAN']))
print(is_contains('cicie',['recycling','cyclic']))
print(is_contains('Утро', ['ночь','день','утрО']))

print(count_calls())
