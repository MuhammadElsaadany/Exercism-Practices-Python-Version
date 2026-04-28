def is_valid(isbn):
    filterlist = list(isbn)
    intlist = []
    if not isbn:
        return False
    
    for i in filterlist:
        if i == "-":
            filterlist.remove(i)
        if str(i).isalpha() and i != "X":
            return False

        
    if filterlist[-1] == "X":
        filterlist.remove("X")
        filterlist.append(10)
        
    for i in filterlist:
        if not str(i).isalpha():
            intlist.append(int(i))

    if len(intlist) != 10:
        return False
    
    return (intlist[0] * 10 + intlist[1] * 9 + intlist[2] * 8 + intlist[3] * 7 + intlist[4] * 6 + intlist[5] * 5 + intlist[6] * 4 + intlist[7] * 3 + intlist[8] * 2 + intlist[9] * 1) % 11 == 0