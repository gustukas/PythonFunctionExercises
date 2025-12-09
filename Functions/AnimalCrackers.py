def animal_crackers(text):
    words = text.split()
    if words[0][0] == words[1][0]:
        return(True)
    else: return(False)
        


print(animal_crackers("Six socks"))