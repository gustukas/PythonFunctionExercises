def find_33(list):
    for i in range(0, len(list)-1):
        if list[i] == 3 and list[i+1] == 3:
            return True
    return False


print(find_33([4,6,3,3]))