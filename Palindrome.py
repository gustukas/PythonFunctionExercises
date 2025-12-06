def palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        return f"The word '{string}' is a palindrome!"
    else:  return f"The word '{string}' is not a palindrome!"

print(palindrome("Racecarr"))