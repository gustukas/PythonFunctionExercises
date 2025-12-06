def spy_game(list):
    newlist = []

    for i in range(0,len(list)):
        if list[i] == 0:
            newlist.append(list[i])
        elif list[i] == 7:
            newlist.append(list[i])
        else: pass

    for i in range(0,len(newlist)):
        if newlist[i] == 0 and newlist[i+1] == 0 and newlist[i+2] == 7:
            return True
        else: return False



print(spy_game([1,7,2,0,4,5,0]))
    