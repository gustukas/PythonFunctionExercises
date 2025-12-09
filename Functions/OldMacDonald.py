def old_mac_donald(name):
    namelist = list(name)
    namelist[0] = namelist[0].upper()
    namelist[3] = namelist[3].upper()
    return "".join(namelist)


print(old_mac_donald("macdonald"))