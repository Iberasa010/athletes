
julie_list = []
james_list = []
sarah_list = []
mickey_list = []

try:
    with open('julie.txt') as julie:
        print(julie.readline())
    with open('james.txt') as james:
        print(james.readline())
    with open('mickey.txt') as mickey:
        print(mickey.readline())
    with open('sarah.txt') as sarah:
        print(sarah.readline())

except FileNotFoundError as fnfe:
    print("The file has not been found")
