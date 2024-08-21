calls = 0
 
def count_calls():
    global calls
    calls = calls +1
 
def string_info(string):
    tekst_ = str(string)
    result = len(tekst_), tekst_.upper(), tekst_.lower()
    count_calls()
    return result
 
def is_contains(string, list_to_search):
    list_to_search = list(list_to_search)
    string = str(string).lower()
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i].lower()) == string:
             result = True
             break
        else:
            result = False
            continue
    return result
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
