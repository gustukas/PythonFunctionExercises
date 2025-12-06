import string
alphabet = set(list(string.ascii_lowercase))

def is_pangram(string):
    newstring = string.lower()
    newstring = newstring.replace(" ","")
    if set(list(newstring)) == alphabet:
        return True
    else: return False

print(is_pangram("The quick brown fox jumps over the lazy dog"))