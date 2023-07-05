from sanitizer import sanitizer
from opener import open_files

try:
    james_data = open_files('james.txt')
    mikey_data = open_files('mikey.txt')
    julie_data = open_files('julie.txt')
    sarah_data = open_files('sarah.txt')

    sorted_s = [sanitizer(elem) for elem in sarah_data]
    sorted_ja = [sanitizer(elem) for elem in james_data]
    sorted_ju = [sanitizer(elem) for elem in julie_data]
    sorted_m = [sanitizer(elem) for elem in mikey_data]

    james = sorted(set(sorted_s))
    mikey = sorted(set(sorted_m))
    julie = sorted(set(sorted_ju))
    sarah = sorted(set(sorted_ja))

    print("Best 3 James times: ")
    print(james[0:3])
    print("Best 3 Mikey times: ")
    print(mikey[0:3])
    print("Best 3 Julie times: ")
    print(julie[0:3])
    print("Best 3 Sarah times: ")
    print(sarah[0:3])

except FileNotFoundError:
    print("The file hasn't been found")
except IOError as ioe:
    print("An error of type " + str(ioe) + " has appeared")
