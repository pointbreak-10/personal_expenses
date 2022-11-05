import re

def check(str):
    # if len(str) < 8:
    #     return False
    # else: --- to be added later 
    cap = re.findall("[A-Z]+", str)
    small = re.findall("[a-z]+",str)
    num = re.findall("[0-9]+",str)

    if len(cap)*len(small)*len(num) != 0:
        return True
    else:
        return False