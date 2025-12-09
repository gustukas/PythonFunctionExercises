try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("TypeError - You must put in numbers, not strings.")