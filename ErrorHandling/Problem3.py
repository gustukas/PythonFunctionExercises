def ask():
    while True:
        try:
            result = int(input("Please put in any number: "))
        except:
            print("Sorry, that is not a number")
        else: return f"Thank you the result is: {result ** 2}"

    

print(ask())