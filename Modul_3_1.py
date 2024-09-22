calls = 0
def count_calls():
    global calls
    wrapper.calls += 1
    return calls
    print(count_calls(calls))

def string_info(string):
    global calls
    calls += 1
    a = len(string)
    b = string.upper()
    c = string.lower()
    return a, b, c
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Доброе утро'))

def is_contains(string,list_to_search):
    global calls
    calls += 1
    a = string.lower()
    b = [s.lower() for s in list_to_search]
    return a in b
print(is_contains('Urban', ['ban', 'BaNaN','urBAN']))
print(is_contains('cicie',['recycling','cyclic']))
print(is_contains('Утро', ['ночь','день','утрО']))


