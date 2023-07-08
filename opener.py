from Athlete import AthleteList


def open_files(athlete_file):
    # This function opens a file and makes it appropriate to work with in the latter
    # parts of the code.
    try:
        with open(athlete_file) as generic_file:
            data = generic_file.readline()
            athlete = data.strip().split(',')
            my_athlete = AthleteList(athlete.pop(0), athlete.pop(0), athlete)
            return my_athlete

    except FileNotFoundError:
        print("Such file does not exist")
    except IOError as ioe:
        print("An error of type " + str(ioe) + " has occurred")
