
try:
    with open('james.txt') as james:
        data = james.readline()
        james_data = data.strip().split(',')
        print(james_data)
    with open('julie.txt') as julie:
        data = julie.readline()
        julie_data = data.strip().split(',')
        print(julie_data)
    with open('mikey.txt') as mikey:
        data = mikey.readline()
        mikey_data = data.strip().split(',')
        print(mikey_data)
    with open('sarah.txt') as sarah:
        data = sarah.readline()
        sarah_data = data.strip().split(',')
        print(sarah_data)

except FileNotFoundError:
    print("The file hasn't been found")
except IOError as ioe:
    print("An error of type " + str(ioe) + " has appeared")
