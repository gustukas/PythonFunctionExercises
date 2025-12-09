def summer_69(list):
    adding = True
    sum = 0
    for i in list:
        if i == 6:
           adding = False
        elif i == 9:
            adding = True
        else: pass
        if adding == True and i != 9:
            sum = sum + i
        else: pass
    return sum

print(summer_69([2, 1, 6, 9, 11]))




