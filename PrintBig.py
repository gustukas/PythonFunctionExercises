bigdict = {"a":"  *  \n * * \n*****\n*   *\n*   *",
           "b":"*** \n*  *\n*** \n*  *\n***",
           "c":" ***\n*\n*\n*\n ***",
           "d":"****\n*   *\n*   *\n*   *\n****",
           "e":"****\n*\n****\n*\n****"}

def print_big(letter):
    return bigdict[letter]

print(print_big("c"))