calls = 0


def count_calls():
    global calls


calls = 4


def string_info(string):
    print(string)


string_info1 = (len('Capybara'))
string_info2 = ('Capybara'.upper())
string_info3 = ('Capybara'.lower())
string_info4 = (len('Armageddon'))
string_info5 = ('Armageddon'.upper())
string_info6 = ('Armageddon'.lower())
string_info([string_info1, string_info2, string_info3])
string_info([string_info4, string_info5, string_info6])


def is_contains(string, list_to_search):
    list_to_search = ('Urban', ['dan', 'BaNaN', 'urBAN'])
    list_to_search_2 = ('cycle', ['recycling', 'cyclic'])
    string = ('Urban', 'urBAN')
    if string[0] in list_to_search or string[0] in list_to_search_2:
        print(True)
    else:
        print(False)
    if string[1] in list_to_search or string[1] in list_to_search_2:
        print(True)
    else:
        print(False)


is_contains(True, False)

print(calls)
