def lesser_of_two_evens(x,y):
    if x % 2 == 0 and y % 2 == 0:
        if x > y:
            return y
        elif y > x:
            return x
        else: return ("Both numbers are equal!")
    elif x % 2 != 0 or y % 2 != 0:
        if x > y:
            return x
        elif x < y:
            return y
        
print(lesser_of_two_evens(1,5))