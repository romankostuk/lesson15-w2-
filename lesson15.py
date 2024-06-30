calls = 0
def count_calls():
    calls =+ 1

def string_info(string):
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        f = 0
        c = list_to_search[i].lower().find(string.lower())
        if c >= 0:
            f += 1
    if f > 0:
        print(True)
    else:
        print(False)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

