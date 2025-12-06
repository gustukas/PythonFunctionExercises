def up_low(string):
    uppercaseletters = []
    lowercaseletters = []

    newstring = list(string)
    for i in newstring:
        if i.isupper():
            uppercaseletters.append(i)
        elif i.islower():
            lowercaseletters.append(i)
    return f"No. of Upper case letters is {len(uppercaseletters)}\nNo. of Lower case letters is {len(lowercaseletters)}"
    
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))