def master_yoda(string):
    newstring = string.split()
    newstring.reverse()
    return " ".join(newstring)

print(master_yoda(""))