def commands(binary_str):
    binarylist = list(binary_str)
    actions = []
    
    if binarylist[4] == "1":
        actions.append("wink")
    if binarylist[3] == "1":
        actions.append("double blink")
    if binarylist[2] == "1":
        actions.append("close your eyes")
    if binarylist[1] == "1":
        actions.append("jump")
    if binarylist[0] == "1":
        actions.reverse()
        
    return actions
