
julie_list = []
james_list = []
sarah_list = []
mickey_list = []

try:
    with open('julie.txt') as julie:
        print(julie.readline())
except FileNotFoundError as fnfe:
    print("The file has not been found")
