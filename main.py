from sanitizer import sanitizer


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
    sorted_ja = []
    sorted_ju = []
    sorted_m = []

    for elem in sarah_data:
        sorted_s.append(sanitizer(elem))
    for elem in mikey_data:
        sorted_m.append(sanitizer(elem))
    for elem in julie_data:
        sorted_ju.append(sanitizer(elem))
    for elem in james_data:
        sorted_ja.append(sanitizer(elem))

    print(sorted(sorted_s, reverse=True))
    print(sorted(sorted_m, reverse=True))
    print(sorted(sorted_ju, reverse=True))
    print(sorted(sorted_ja, reverse=True))


except FileNotFoundError:
    print("The file hasn't been found")
except IOError as ioe:
    print("An error of type " + str(ioe) + " has appeared")
