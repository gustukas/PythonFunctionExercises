def paper_doll(string):
    string = list(string)
    d = 0
    f = []
    for i in string:
        l = i*3
        d = d+1
        f.append(l)
    return "".join(f)


print(paper_doll("Hello World"))