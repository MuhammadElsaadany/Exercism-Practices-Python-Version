def recite(start_verse, end_verse):
    test = ["",
           "house",
           "malt that lay in the ",
           "rat that ate the ",
           "cat that killed the ",
           "dog that worried the ",
           "cow with the crumpled horn that tossed the ",
           "maiden all forlorn that milked the ",
           "man all tattered and torn that kissed the ",
           "priest all shaven and shorn that married the ",
           "rooster that crowed in the morn that woke the ",
           "farmer sowing his corn that kept the ",
           "horse and the hound and the horn that belonged to the "]
    buffer = []
    bufferino = []
    if start_verse == end_verse:
        starting = 0
        buffer.append("This is the ")
        while starting != start_verse:
            zew = start_verse - starting
            buffer.append(test[zew])
            starting += 1
        buffer.append(" that Jack built.")
        befo = ["".join(buffer)]
        return befo
    else:
        while not start_verse > end_verse:
            starting = 0
            buffer = []
            buffer.append("This is the ")
            while starting != start_verse:
                zew = start_verse - starting
                buffer.append(test[zew])
                starting += 1
            buffer.append(" that Jack built.")
            start_verse += 1
            bufferino.append("".join(buffer))
        return bufferino