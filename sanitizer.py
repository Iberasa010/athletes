
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



