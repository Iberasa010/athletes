
def sanitizer(time_string):
    # This function turns strings separated with :, - or . and turns them into strings separated by :
    # It's supposed to work specifically for the james, julie and mikey files which contain those characters
    # as separators"""
    if ':' in time_string:
        return time_string
    elif '.' in time_string:
        splitter = '.'
        (mins, secs) = time_string.split(splitter)
    else:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


try:
    with open('james.txt') as james:
        data = james.readline()
        james_data = data.strip().split(',')
        # print(james_data)
    with open('julie.txt') as julie:
        data = julie.readline()
        julie_data = data.strip().split(',')
        # print(julie_data)
    with open('mikey.txt') as mikey:
        data = mikey.readline()
        mikey_data = data.strip().split(',')
        # print(mikey_data)
    with open('sarah.txt') as sarah:
        data = sarah.readline()
        sarah_data = data.strip().split(',')
        # print(sarah_data)

    sorted_s = []
    for elem in sarah_data:
       sorted_s.append(sanitizer(elem))

except FileNotFoundError:
    print("The file hasn't been found")
except IOError as ioe:
    print("An error of type " + str(ioe) + " has appeared")
