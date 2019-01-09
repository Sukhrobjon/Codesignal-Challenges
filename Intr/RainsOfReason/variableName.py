import re

def variableName(name):

    if not name[0].isdigit():
        if(bool(re.match("^[A-Za-z0-9_]*$", name))):
            return True
    return False
