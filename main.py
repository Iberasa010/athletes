from opener import open_files

try:
    james_data = open_files('james2.txt')
    mikey_data = open_files('mikey2.txt')
    julie_data = open_files('julie2.txt')
    sarah_data = open_files('sarah2.txt')

    print("The athlete's data are: ")
    print("James:")
    print(james_data.top3())
    print("Sarah")
    print(sarah_data.top3())
    print("Julie")
    print(julie_data.top3())
    print("Mikey")
    print(mikey_data.top3())

except FileNotFoundError:
    print("The file hasn't been found")
except IOError as ioe:
    print("An error of type " + str(ioe) + " has appeared")
